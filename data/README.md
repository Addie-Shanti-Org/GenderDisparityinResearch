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

## Dataset registry

### r/WomensHealth posts and comments

- **Source:** Reddit archive collected by Watchful1, distributed via [Academic Torrents](https://academictorrents.com/); mirrored on [Kaggle](https://www.kaggle.com/datasets/addieg/reddit-postscomments-rwomenshealth-as-of-dec-25/data)
- **Date pulled:** through December 2025
- **Where it lives in this repo:** `data/raw/subreddits25/` (gitignored) — see [`notebooks/Reddit_Data/README.md`](../notebooks/Reddit_Data/README.md) for the expected file layout
- **Ethics / consent notes:** usernames dropped during cleaning; no post text, title, or comment content appears in any published output, only aggregate counts per topic. See the [root README](../README.md#ethics-and-data-notice) for full notes.
- **How to fetch:** download the Kaggle mirror above into `data/raw/`, or pull the original archive from Academic Torrents.

### PubMed publication records

- **Source:** U.S. National Library of Medicine (PubMed), queried via [PaperScraper](https://github.com/jannisborn/paperscraper); mirrored on [Kaggle](https://www.kaggle.com/datasets/shanti33/womens-health-pubmed-dataset-1786-2026)
- **Date pulled:** covers 1786–2026
- **Where it lives in this repo:** `data/raw/` (gitignored)
- **Ethics / consent notes:** public metadata only, pulled through PubMed's public API.
- **How to fetch:** download the Kaggle mirror, or rerun `notebooks/Article_Data_APIs/paperscraper.ipynb`.

### ClinicalTrials.gov trial records

- **Source:** ClinicalTrials.gov, queried via [PyTrials](https://pypi.org/project/pytrials/); mirrored on [Kaggle](https://www.kaggle.com/datasets/shanti33/womens-health-clinical-trials-dataset-1968-2026/data)
- **Date pulled:** covers 1968–2026
- **Where it lives in this repo:** `data/raw/` (gitignored)
- **Ethics / consent notes:** public metadata only, pulled through ClinicalTrials.gov's public API.
- **How to fetch:** download the Kaggle mirror, or rerun `notebooks/Article_Data_APIs/pytrials.ipynb`.

### `data/processed/topic_summary.csv`

- **What it is:** 49 rows, one per topic, with post/paper/trial counts and the sex-applicability label — the single file needed to reproduce the regression models and every figure.
- **Produced by:** the `notebooks/Reddit_Data/` pipeline (01–06) joined against the PubMed and ClinicalTrials.gov pulls.
- **Consumed by:** `notebooks/RCode_Final_Models/Data_510_Capstone.Rmd`.

`data/processed/topic_info_0.csv` and `topic_info_1.csv` are intermediate BERTopic outputs, kept for reference.
