# `notebooks/`

All analysis notebooks, in three pipelines:

```
notebooks/
  Reddit_Data/          # clean posts, topic-model them, count and map topics (run 01-06 in order)
  Article_Data_APIs/    # pull and process PubMed and ClinicalTrials.gov data by keyword
  RCode_Final_Models/   # negative binomial regression + final figures
```

- **[`Reddit_Data/`](Reddit_Data/)** — turns the raw r/WomensHealth archive into per-topic post counts. See its own [README](Reddit_Data/README.md) for run order and setup.
- **`Article_Data_APIs/`** — `paperscraper.ipynb` and `pytrials.ipynb` pull publication and trial records by keyword; the other notebooks in this folder explore and transform that raw pull into keyed, joinable data.
- **`RCode_Final_Models/`** — `Data_510_Capstone.Rmd` fits the regression models and renders the figures used in the write-up, reading from `data/processed/topic_summary.csv`.

See the [project root README](../README.md) for the full pipeline and how these stages connect.
