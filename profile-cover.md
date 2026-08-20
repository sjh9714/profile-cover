---
name: profile-cover
description: >
  Design a GitHub profile README (the special username/username repo) as
  an editorial page with kerned serif mastheads. Use when the user wants
  their GitHub profile designed, a profile README, a personal masthead,
  or to replace widget and badge clutter. This flat file is the
  self-contained version for harnesses that discover a single skill
  file; the full skill with three archetype references lives in
  skills/profile-cover/ at https://github.com/sjh9714/profile-cover
license: MIT
---

# profile-cover (flat)

You design a GitHub profile README as an editorial page. Display type
is generated as path-outlined SVG by two small scripts from the source
repo, so it renders identically through GitHub's image proxy on every
OS. Everything that should be clickable stays GitHub-native markdown.
No image model, no third-party stats services, nothing that can 503
into a broken image.

## Setup

```sh
pip install fonttools uharfbuzz
mkdir -p pc && cd pc
base=https://raw.githubusercontent.com/sjh9714/profile-cover/main/skills/profile-cover
curl -sO $base/scripts/shape.py
curl -sO $base/scripts/make_masthead.py
curl -sO $base/scripts/check_profile.py
curl -s -o fraunces.ttf $base/assets/fraunces.ttf
```

## Workflow

1. Interview the user: name or handle for the masthead, one line of what
   they do, 3 to 6 things worth pinning (repos, posts, a site), links.
2. Generate the masthead and one section strip per README section:
   `python3 make_masthead.py --font fraunces.ttf --text "NAME" --label "ONE LINE" --out masthead`
   writes `masthead-light.svg` and `masthead-dark.svg`. Add `--center`
   for a centered archetype; default is flush left. Section strips:
   same command with `--text "Section"` at a smaller `--size`.
3. Assemble `README.md`. Each SVG pair goes in as:
   `<picture><source media="(prefers-color-scheme: dark)" srcset="masthead-dark.svg"><img src="masthead-light.svg" width="900" alt="NAME"></picture>`
   Everything else is plain markdown: lists of links with one honest
   line each, no tables with empty headers, no inline styles (GitHub
   strips them), no badge rows.
4. Check before delivering: `python3 check_profile.py README.md *.svg`
5. Tell the user to put README.md and the SVGs in their
   `username/username` repo.

## Hard rules

- Light and dark SVGs always ship as a pair; accents pass 4.5:1 against
  GitHub's page colors (#FFFFFF light, #0D1117 dark).
- No external resources inside any SVG. Text is path outlines, never a
  font-family reference.
- No label text under 12.5px, the mobile legibility floor.
- No live counts or "this week" copy unless the user has a refresh
  Action; stale numbers read worse than none.
- Third-party dynamic images (stats cards, contribution graphs) stay
  out; they rate-limit and 503. If the user insists, warn once.

For the three archetype references (shipping ledger, build log,
stewardship), shipped examples, and the deterministic checker in CI,
see https://github.com/sjh9714/profile-cover
