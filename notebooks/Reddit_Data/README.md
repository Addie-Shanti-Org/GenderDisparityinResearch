# Reddit data pipeline

Notebooks that turn the raw r/WomensHealth archive into topic counts, then link those topics to the PubMed and ClinicalTrials.gov data. Run them in order. Each one reads what the last one wrote.

All paths are relative to this folder, so run the notebooks from `notebooks/Reddit_Data/`.

| Notebook | What it does | Output |
|---|---|---|
| `01_clean_data.ipynb` | Filters to English self-posts, cleans and tokenizes the text | `data/interim/cleaned_submissions.parquet` |
| `02_frequency_analysis.ipynb` | Keyword and bigram counts, keyness against general English | `data/processed/keyword_frequencies.csv` |
| `03_bertopic.ipynb` | Clusters posts by meaning to find discussion topics | `data/interim/topic_info.csv` |
| `04_topic_specific_counts.ipynb` | Maps informal language to topics and counts posts per topic | `data/processed/topic_counts.csv` |
| `05_mapping_research_reddit.ipynb` | Links research keywords to Reddit topics, loads staging table | `data/interim/matched_topics.parquet` |
| `06_assign_main_topic.ipynb` | Applies the topic hierarchy so each item gets exactly one topic | `data/processed/one_topic/` |

## Before you start

Unpack the raw archive. `WomensHealth_submissions.zst` lives in `data/raw/subreddits25/`. Decompress it to `data/interim/subreddits/WomensHealth/submissions`.

Install dependencies from the project `requirements.txt`.

Notebooks 05 and 06 connect to the PostgreSQL database. Copy `.env.example` to `.env` at the project root and fill in the credentials. `.env` is gitignored and should stay that way.

Notebook 03 is much faster with a GPU.
