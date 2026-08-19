# Archetype: shipping ledger

For people who release small things often. Left-aligned masthead with
an optional accent stamp, then a three-column ledger table where every
project name is a link.

## Generate the strips

```sh
python3 scripts/make_masthead.py masthead \
  --name "Mia Tan" \
  --eyebrow "SINGAPORE · ONE SMALL TOOL EVERY WEEK" \
  --tagline "Tiny products, honest changelogs, zero venture capital." \
  --accent-light "#B3382C" --accent-dark "#E0796A" \
  --out masthead
python3 scripts/make_masthead.py section \
  --title "Shipping ledger" --note "MOST RECENT FIRST" \
  --accent-light "#B3382C" --accent-dark "#E0796A" \
  --out ledger
```

The `--stamp` flag is available but counts as decaying copy; only use
it when the user also sets up a refresh Action.

## README skeleton

```markdown
<picture><source media="(prefers-color-scheme: dark)" srcset="masthead-dark.svg"><img src="masthead-light.svg" width="900" alt="NAME, tagline"></picture>

One or two flush-left sentences in the user's voice. No inline styles.

<picture><source media="(prefers-color-scheme: dark)" srcset="ledger-dark.svg"><img src="ledger-light.svg" width="900" alt="Shipping ledger"></picture>

| Project | What it is | |
|---|---|---|
| **[name](url)** | One honest line | `2026-08` |

**Elsewhere.** [Blog](url) · [Now page](url)
```

Table rules: header row must have real labels (an empty header renders
as a blank strip), dates as `YYYY-MM` code spans, 3-6 rows, most
recent first.

## Accent pairs that pass the checker

crimson #B3382C / #E0796A · slate #46627F / #9DB4CF · moss #4A6B3A / #96BB80
