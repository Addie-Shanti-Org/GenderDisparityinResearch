# `notebooks/`

Exploratory and reporting notebooks live here. Suggested naming:

```
notebooks/
  W04-exploration-<topic>.ipynb     # EDA aligned with the M1 proposal
  W05-feasibility-<dataset>.ipynb
  W07-data-summary.ipynb            # M2 milestone artifact
  W10-poster-figures.ipynb          # M3 milestone artifact
  W12-writeup-figures.ipynb         # M4 milestone artifact
```

Conventions:

- Keep one notebook per question. Long, kitchen-sink notebooks are a smell.
- Restart-and-run-all before committing; do not commit a notebook whose outputs are out of order.
- Heavy reusable code belongs in [`../src/`](../src/), not pasted between notebooks.
