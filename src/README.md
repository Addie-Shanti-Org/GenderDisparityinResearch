# `src/`

Project source code lives here: ingestion scripts, feature engineering, modeling, evaluation, plotting helpers.

Suggested layout (adapt to fit your project):

```
src/
  ingest/        # scripts that pull raw data into data/raw/
  features/      # build features from data/raw/ into data/processed/
  models/        # training, evaluation, and inference
  viz/           # plotting and reporting helpers
  utils/         # shared helpers
```

If your project is primarily notebook-driven, you can collapse this folder into a single `src/` module of helpers that your notebooks import, and put the analytical narrative in [`../notebooks/`](../notebooks/).
