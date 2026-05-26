# `data/`

Project data lives here. The repo root `.gitignore` excludes large or sensitive subfolders by default. The structure below is the convention you should follow.

```
data/
  raw/         # original inputs, never edited in place        (gitignored)
  external/    # third-party data you did not generate         (gitignored)
  interim/     # intermediate scratch outputs                  (gitignored)
  processed/   # cleaned, analysis-ready snapshots (committable if small)
  README.md    # describe each dataset: source, license, date, size
  SCHEMA.md    # describe processed dataset schemas once they stabilize
```

## What to **always** commit

- This `README.md` describing every dataset, with: source URL or contact, license, date pulled, approximate size, who in the team owns it, and any ethics / consent notes.
- A `SCHEMA.md` documenting the columns, types, and units of your processed datasets, once they stabilize.
- Small (< 1 MB) reproducible processed snapshots under `data/processed/` if your analysis depends on a specific version.

## What to **never** commit

- Personally identifiable information (PII), protected health information (PHI), or any data subject to a data use agreement that forbids redistribution.
- Credentials, API keys, OAuth tokens, or `.env` files.
- Multi-megabyte raw downloads. Document how to fetch them in this README instead.

## Dataset registry (fill in)

### Dataset 1: <name>

- **Source:** <URL or contact>
- **License:** <name and short summary>
- **Date pulled:** <YYYY-MM-DD>
- **Approximate size:** <rows, columns, bytes>
- **Owner on this project:** <name>
- **Where it lives in this repo:** `data/raw/<name>/` (gitignored) or `data/processed/<name>.csv`
- **Ethics / consent notes:** <PII? consent process? data use agreement?>
- **How to fetch (for a teammate cloning fresh):** <command, script, or contact>

### Dataset 2: <name>

- ...
