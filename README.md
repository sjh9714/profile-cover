<picture><source media="(prefers-color-scheme: dark)" srcset="docs/hero-dark.svg"><img src="docs/hero-light.svg" width="900" alt="profile-cover, kerned serif mastheads for GitHub profiles"></picture>

**An agent skill that designs your GitHub profile README as an
editorial page.** The masthead you see above is the product: kerned
Fraunces converted to SVG paths by the bundled scripts, light and dark
pairs, zero external resources, so it renders identically through
GitHub's image proxy on every OS and can never show a broken image.

[한국어](README.ko.md)

## Why not widgets

Most profile READMEs are a stack of third-party stats cards and badge
rows. They rate-limit, they 503, they all look the same. profile-cover
replaces the clutter with typography. Everything that should be a link
stays plain markdown, so your pinned work is clickable, indexable, and
theirs to keep loading forever.

Three archetypes ship with the skill. These strips are live SVGs
rendered by GitHub right now, not screenshots:

<picture><source media="(prefers-color-scheme: dark)" srcset="skills/profile-cover/assets/examples/indiehacker-masthead-dark.svg"><img src="skills/profile-cover/assets/examples/indiehacker-masthead-light.svg" width="900" alt="Shipping ledger archetype, for people who release small things often"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="skills/profile-cover/assets/examples/student-masthead-dark.svg"><img src="skills/profile-cover/assets/examples/student-masthead-light.svg" width="900" alt="Build log archetype, for learning in public"></picture>

<picture><source media="(prefers-color-scheme: dark)" srcset="skills/profile-cover/assets/examples/maintainer-masthead-dark.svg"><img src="skills/profile-cover/assets/examples/maintainer-masthead-light.svg" width="900" alt="Stewardship archetype, for maintainers of one serious thing"></picture>

## Install

```sh
npx skills add sjh9714/profile-cover
pip install fonttools uharfbuzz
```

Then, in any session:

> Design my GitHub profile README.

The agent interviews you, picks an archetype, generates the masthead
and section strips with the bundled scripts, assembles a
GitHub-native README.md, and runs the deterministic checker before you
see anything.

## What the checker enforces

- Accent colors come in light/dark pairs, both passing 4.5:1 contrast
  against GitHub's page colors
- No external resources in any SVG, no inline styles in the markdown
  (GitHub strips them), no empty table header rows
- No labels under 12.5px, the mobile legibility floor
- Warnings on decaying copy ("this week", live counts) unless paired
  with a refresh Action, and on third-party dynamic images

## Sibling project

[repo-cover](https://github.com/sjh9714/repo-cover) designs the social
preview card for a repository the same way. Same design language, same
checker discipline.

## License

MIT. Fraunces is bundled under the SIL Open Font License, see
`skills/profile-cover/assets/OFL.txt`.
