# Contributing

- **Show a profile.** Open a showcase issue; good ones get linked from
  the README with credit.
- **Propose an archetype.** One reference file plus generator flags in
  make_masthead.py, two shipped example strips passing the checker,
  and a distinct silhouette. If a thumbnail could be mistaken for an
  existing archetype, it is a variant, not an archetype.
- **Checker rules.** A new check needs one failing and one passing
  fixture. Python stdlib only in check_profile.py; the shaping scripts
  may use fonttools and uharfbuzz.
- One archetype or one fix per PR. Match the prose style, no em-dashes.
