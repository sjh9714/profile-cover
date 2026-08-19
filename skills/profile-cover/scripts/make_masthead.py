#!/usr/bin/env python3
"""Generate a kerned, path-outlined masthead or section-head SVG pair.

The display type is HarfBuzz-shaped Fraunces converted to paths, so the
SVG renders identically everywhere, including through GitHub's camo
proxy, with zero external resources. Small labels use system font
stacks, which SVG-in-img resolves per viewer OS.

Usage:
  python3 make_masthead.py masthead --name "Mia Tan" \
    --eyebrow "SINGAPORE · ONE SMALL TOOL EVERY WEEK" \
    --tagline "Tiny products, honest changelogs." \
    --accent-light "#B3382C" --accent-dark "#E0796A" \
    --stamp "THIS WEEK · W34" --out mia-masthead
  python3 make_masthead.py masthead --center --name "Alex Rivera" ...
  python3 make_masthead.py section --title "Shipping ledger" \
    --note "MOST RECENT FIRST" --accent-light ... --out mia-ledger

Writes <out>-light.svg and <out>-dark.svg. Requires:
  pip install fonttools uharfbuzz
"""
import argparse
import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))
from shape import shape_to_paths

HERE = pathlib.Path(__file__).parent
FONT = str(HERE.parent / "assets" / "fraunces.ttf")
AX = {"wght": 560, "opsz": 144, "SOFT": 0, "WONK": 0}
AX_LIGHT = {"wght": 400, "opsz": 144, "SOFT": 0, "WONK": 0}
MONO = "ui-monospace,SFMono-Regular,Menlo,Consolas,monospace"

INK = {"light": "#1D1A16", "dark": "#EDEAE4"}
MUTED = {"light": "#6B655C", "dark": "#9A938A"}
HAIR = {"light": "#D9D4CB", "dark": "#3A362F"}
# Minimum small-label size. GitHub renders READMEs at ~890px, mobile web
# scales a 900px strip to ~40%, so labels below 12.5px die on phones.
MIN_LABEL = 12.5


def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
            f'viewBox="0 0 {w} {h}">{body}</svg>')


def masthead(a, theme):
    accent = a.accent[theme]
    if a.center:
        paths, wid = shape_to_paths(FONT, a.name, 72, AX_LIGHT)
        cx = 450 - wid / 2
        body = f'''
<line x1="330" y1="10" x2="570" y2="10" stroke="{HAIR[theme]}" stroke-width="1"/>
<text x="450" y="40" text-anchor="middle" font-family="{MONO}" font-size="{MIN_LABEL}"
  letter-spacing="3.5" fill="{MUTED[theme]}">{a.eyebrow}</text>
<g fill="{INK[theme]}" transform="translate({cx:.0f},124)">{"".join(paths)}</g>
<text x="450" y="164" text-anchor="middle" font-family="{MONO}" font-size="14"
  fill="{MUTED[theme]}">{a.tagline}</text>
<rect x="438" y="184" width="24" height="2.5" fill="{accent}"/>'''
        return svg(900, 196, body)
    paths, wid = shape_to_paths(FONT, a.name, 76, AX)
    stamp = ""
    if a.stamp:
        stamp = (f'<text x="900" y="18" text-anchor="end" font-family="{MONO}" '
                 f'font-size="13" letter-spacing="2.5" fill="{accent}">{a.stamp}</text>')
    body = f'''
<text x="1" y="18" font-family="{MONO}" font-size="13" letter-spacing="2.5"
  fill="{MUTED[theme]}">{a.eyebrow}</text>{stamp}
<g fill="{INK[theme]}" transform="translate(0,110)">{"".join(paths)}</g>
<text x="2" y="152" font-family="{MONO}" font-size="14.5" fill="{MUTED[theme]}">{a.tagline}</text>
<line x1="1" y1="176" x2="900" y2="176" stroke="{HAIR[theme]}" stroke-width="1"/>'''
    return svg(900, 182, body)


def section(a, theme):
    accent = a.accent[theme]
    paths, wid = shape_to_paths(FONT, a.title, 30, AX)
    if a.center:
        x = 450 - wid / 2
        note = (f'<text x="450" y="64" text-anchor="middle" font-family="{MONO}" '
                f'font-size="{MIN_LABEL}" letter-spacing="2.5" fill="{MUTED[theme]}">{a.note}</text>')
        return svg(900, 76, f'<g fill="{INK[theme]}" transform="translate({x:.0f},38)">{"".join(paths)}</g>{note}')
    body = f'''<g fill="{INK[theme]}" transform="translate(0,36)">{"".join(paths)}</g>
<text x="900" y="34" text-anchor="end" font-family="{MONO}" font-size="{MIN_LABEL}"
  letter-spacing="2.5" fill="{accent}">{a.note}</text>
<line x1="1" y1="52" x2="900" y2="52" stroke="{HAIR[theme]}" stroke-width="1"/>'''
    return svg(900, 60, body)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kind", choices=["masthead", "section"])
    ap.add_argument("--name", default="")
    ap.add_argument("--title", default="")
    ap.add_argument("--eyebrow", default="")
    ap.add_argument("--tagline", default="")
    ap.add_argument("--note", default="")
    ap.add_argument("--stamp", default="")
    ap.add_argument("--center", action="store_true")
    ap.add_argument("--accent-light", required=True)
    ap.add_argument("--accent-dark", required=True)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()
    a.accent = {"light": a.accent_light, "dark": a.accent_dark}
    fn = masthead if a.kind == "masthead" else section
    for theme in ("light", "dark"):
        path = pathlib.Path(f"{a.out}-{theme}.svg")
        path.write_text(fn(a, theme))
        print("wrote", path)


if __name__ == "__main__":
    main()
