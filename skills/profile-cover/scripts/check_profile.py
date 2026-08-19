#!/usr/bin/env python3
"""Deterministic checks for a profile-cover README and its SVG strips.

Usage: python3 check_profile.py README.md [svg files...]
Exit 0 = pass, 1 = any FAIL.
"""
import re
import sys

DECAY = [r"THIS WEEK", r"LAST WEEK", r"YESTERDAY", r"\bW\d\d\b",
         r"DAYS? AGO", r"CURRENTLY", r"RIGHT NOW"]


def luminance(hexcolor):
    rgb = [int(hexcolor[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    lin = [c / 12.92 if c <= .04045 else ((c + .055) / 1.055) ** 2.4 for c in rgb]
    return .2126 * lin[0] + .7152 * lin[1] + .0722 * lin[2]


def contrast(a, b):
    la, lb = sorted((luminance(a), luminance(b)), reverse=True)
    return (la + .05) / (lb + .05)


def check_svg(path):
    ok = True
    src = open(path, encoding="utf-8").read()
    def fail(m):
        nonlocal ok; ok = False; print(f"  FAIL  {path}: {m}")
    def warn(m):
        print(f"  WARN  {path}: {m}")
    for url in re.findall(r"https?://[^\s\"'()]+", src):
        host = url.split("/")[2]
        if host == "www.w3.org":
            continue
        fail(f"external resource: {host}")
    if re.search(r'<rect[^>]+width="900"[^>]+height="\d+"[^>]+fill="#', src) \
            and 'fill="none"' not in src[:400]:
        m = re.search(r'<rect x="0" y="0" width="900"', src)
        if m:
            warn("full-bleed background rect; transparent merges better with GitHub chrome")
    dark = "-dark.svg" in path
    bg = "#0D1117" if dark else "#FFFFFF"
    for size, color in re.findall(r'font-size="([\d.]+)"[^>]*fill="(#[0-9A-Fa-f]{6})"', src):
        if float(size) < 12.5:
            fail(f"label {size}px under the 12.5px mobile floor")
        r = contrast(bg, color)
        if float(size) < 16 and r < 4.5:
            fail(f"label {color} at {size}px is {r:.2f}:1 on {bg}, needs 4.5:1")
    for pat in DECAY:
        if re.search(pat, src):
            warn(f"decaying copy matches /{pat}/; pair it with a refresh Action or remove")
    return ok


def check_md(path):
    ok = True
    src = open(path, encoding="utf-8").read()
    def fail(m):
        nonlocal ok; ok = False; print(f"  FAIL  {path}: {m}")
    def warn(m):
        print(f"  WARN  {path}: {m}")
    if "style=" in src:
        fail("inline style attribute; GitHub strips it, layout will not survive")
    for base in re.findall(r'srcset="([^"]+)-dark\.svg"', src):
        if f'{base}-light.svg' not in src:
            fail(f"dark srcset without light fallback for {base}")
    if "<picture>" not in src:
        warn("no light/dark picture pair; profile will ignore viewer theme")
    if re.search(r"\|\s*\|\s*\|\s*\|", src.splitlines()[0] if src else ""):
        pass
    for line in src.splitlines():
        if re.fullmatch(r"\|(\s*\|)+", line.strip()):
            fail("empty table header row renders as a visible blank strip")
    if "img.shields.io" in src or "github-readme-stats" in src:
        warn("third-party dynamic image; outages show as broken images on your profile")
    return ok


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    results = []
    for p in sys.argv[1:]:
        results.append(check_md(p) if p.endswith(".md") else check_svg(p))
        print(f"{'PASS' if results[-1] else 'FAIL'}  {p}")
    sys.exit(0 if all(results) else 1)
