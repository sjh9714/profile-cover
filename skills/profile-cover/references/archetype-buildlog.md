# Archetype: build log

For students and people learning in public. Left-aligned masthead, then
a dated list where every entry links to the project and to a
postmortem or notes.

## Generate the strips

```sh
python3 scripts/make_masthead.py masthead \
  --name "Jun Park" \
  --eyebrow "SEOUL · CS SENIOR · NEW GRAD 2027" \
  --tagline "Systems coursework in public, one build log at a time." \
  --accent-light "#2E5E9E" --accent-dark "#84ABDF" \
  --out masthead
python3 scripts/make_masthead.py section \
  --title "Build log" --note "EVERY PROJECT HAS A POSTMORTEM" \
  --accent-light "#2E5E9E" --accent-dark "#84ABDF" \
  --out log
```

## README skeleton

```markdown
<picture><source media="(prefers-color-scheme: dark)" srcset="masthead-dark.svg"><img src="masthead-light.svg" width="900" alt="NAME, tagline"></picture>

One flush-left sentence about how they learn.

<picture><source media="(prefers-color-scheme: dark)" srcset="log-dark.svg"><img src="log-light.svg" width="900" alt="Build log"></picture>

- `2026-06` — **[project](url)**, what it is in one line. [What broke](notes-url)
- `2026-03` — **[project](url)**, one line. [Notes](url)
```

List rules: newest first, every entry carries a date code span, the
second link is the differentiator (postmortem, notes, writeup); if the
user has no notes for an item, drop the second link rather than
inventing one.

The list separator between date and name is a plain markdown em dash
inside the line; it renders as the archetype's house style.
