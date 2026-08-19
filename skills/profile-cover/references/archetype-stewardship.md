# Archetype: stewardship

For maintainers whose energy goes into one serious thing. Centered
frontispiece masthead with a short rule above the eyebrow and an
accent bar below the tagline, then a centered section head and a short
markdown body naming the flagship first.

## Generate the strips

```sh
python3 scripts/make_masthead.py masthead --center \
  --name "Alex Rivera" \
  --eyebrow "MAINTAINS QUERYKIT SINCE 2019" \
  --tagline "One library, maintained like a garden." \
  --accent-light "#4A6B3A" --accent-dark "#96BB80" \
  --out masthead
python3 scripts/make_masthead.py section --center \
  --title "Stewardship" --note "REVIEWS WITHIN 48 HOURS" \
  --accent-light "#4A6B3A" --accent-dark "#96BB80" \
  --out stewardship
```

Only promise a review cadence in the note if the user actually keeps
one; ask.

## README skeleton

```markdown
<picture><source media="(prefers-color-scheme: dark)" srcset="masthead-dark.svg"><img src="masthead-light.svg" width="900" alt="NAME, tagline"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="stewardship-dark.svg"><img src="stewardship-light.svg" width="900" alt="Stewardship"></picture>

Most of my energy goes into **[flagship](url)** and the people who
depend on it. One honest scale fact if the user provides one.

- **[satellite-repo](url)** — what it does for the flagship
- **[rfc-log](url)** — public design notes before breaking changes

[Sponsor link or contact](url) if the user has one.
```

The masthead uses the lighter Fraunces weight (the script handles it
with `--center`); do not bold the centered name.
