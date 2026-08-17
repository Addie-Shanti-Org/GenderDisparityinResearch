# <Gender Disparity in Research>

> What women’s health symptoms and conditions are most discussed on r/WomensHealth, and to what extent are these topics represented in clinical research on PubMed and ClinicalTrials.gov?

## Quick reference

| Field | Value |
|-------|-------|
| Owner team | Addison Gage and Shanti Brodnick |
| Owner Product Lead | Shanti Brodnick |
| Peer Stakeholder POs | Mary Krouse, Aaron Perez Sales, Bradley Allen |
| Studio Session | 3 |
| GitHub repo | https://github.com/Addie-Shanti-Org/GenderDisparityinResearch |
| GitHub Projects board | https://github.com/orgs/Addie-Shanti-Org/projects/3 |
| Discord category | `#Project 2: Addison & Shanti` |
| Instructor / Sponsor | Lucas Cordova (`LucasCordova` on GitHub) |

## What this repo contains

| Path | Purpose |
|------|---------|
| [`CHARTER.md`](CHARTER.md) | Studio Charter: vision, mission, context, success criteria, working agreements, SLAs, DoR / DoD. Committed at the end of the week 3 Studio Charter session. |
| [`BACKLOG.md`](BACKLOG.md) | Human-readable mirror of the GitHub Projects board. |
| [`studio/briefs/`](studio/briefs/) | Weekly Studio Briefs from peer POs (`W<NN>-<peer>.md`). |
| [`studio/critiques/`](studio/critiques/) | Weekly Studio Critiques from peer POs (`W<NN>-<peer>.md`). |
| [`src/`](src/) | Working code (scripts, modules). |
| [`notebooks/`](notebooks/) | Exploratory and reporting notebooks. |
| [`data/`](data/) | Project data. Raw inputs are `.gitignored` by default; see `data/README.md`. |
| [`deliverables/`](deliverables/) | Milestone deliverables: proposal, data summary, poster, write-up. |

## How this project runs (DS3 in one paragraph)

This project is run as a **DS3 studio**: the owner team is paired with two or three **peer Stakeholder POs** drawn from adjacent capstone projects. Every week the peer POs file a **Studio Brief** for the next iteration and a **Studio Critique** of the last iteration. The owner team commits an **Iteration Review** here in `README.md` before each class. See the [Studio Session weekly ritual](https://courses.lpcordova.phd/data510/project-framework/weekly-ritual.html) for the cadence and [Studio Charter](https://courses.lpcordova.phd/data510/project-framework/charter-inception.html) for the inception session.

---

# Iteration Reviews

One subsection per class week. The owner team commits the new section **before each class** so peer POs can read it before filing the next Brief and Critique. Use the template at the bottom of this file for any extra weeks you add.

## Week 4 -- Proposal milestone (M1)

**Iteration ending:** 6/7/2026
**Milestone tag in focus:** `M1-proposal`

**Completed PBIs**
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/1
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/2

**In-flight (carrying across the boundary)**
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/3

**Stakeholder response log**
- Studio Brief from Bradley: adopted = Citation fixes, making main purpose clear, fixing boilerplate sections.  Deferred = Formal tone (editorializing, contracting) for final write-up. declined (with reason) = ...
- Studio Brief from Aaron: adopted = ..., deferred = ..., declined (with reason) = ...
- Studio Brief from Mary: adopted = ..., deferred = ..., declined (with reason) = ...

**Plan for next iteration**
Top PBIs (with milestone tags):
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/4
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/5
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/6

**Risks and impediments**
- Some risks include issues with data collection. One is scraping taking longer than anticipated due to rate-limiting, which we will mitigate by scheduling scraping to run overnight for long periods of time. Another risk is unexpected access issues, which we mitigate by maintaining multiple data sources as backup options. Transforming and storing the data can be computationally expensive, so we will use Railway to host our database and upgrade our plan if necessary. 

## Week 5 - 7

**Iteration ending:** <June 28>
**Milestone tag in focus:** `M2-data-summary`

**Completed PBIs**
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/5
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/4
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/6

**Stakeholder response log**
- Studio Brief Mary: Will adopt: Inclusion gender language, mention this in ethics
- Studio Brief Bradley: Will adopt: Structure analysis of data sources and carefully crafting boolean searches.

**Plan for next iteration**
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/9
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/10

**Risks and impediments**
- Due to the amount of articles and data, our main risk and implementation is capturing all of the studies published about topics that we are interested in.


**Retrospective (milestone boundary)**
- What worked: ...
- What did not: ...
- One change for next iteration: ...

## Week 8 - 10

**Iteration ending:** July 12
**Milestone tag in focus:** `M3-poster-draft`

**Completed PBIs**
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/6
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/12
- Progress on 9, 10

**Stakeholder response log**
- ...

**Plan for next iteration**
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/14
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/9
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/10
- https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/issues/13

**Risks and impediments**
- Large amounts of article data

**Retrospective (milestone boundary)**
- What worked: We really like our poster design.
- What did not: Poster making takes a lot of time.
- One change for next iteration: Allocate time to writing up the paper and finalizing the poster.

## Week 11-12 -- Write-up rough-draft milestone (M4)

**Iteration ending:** August 2
**Milestone tag in focus:** `M4-writeup-draft`

**Completed PBIs**
- ...

**Stakeholder response log**
- ...

**Plan for next iteration**
- ...

**Risks and impediments**
- ...

**Retrospective (milestone boundary)**
- What worked: ...
- What did not: ...
- One change for next iteration: ...

## Week 13-14 -- Final write-up and poster (M5)

**Iteration ending:** <date>
**Milestone tag in focus:** `M5-final`

**Completed PBIs**
- ...

**Stakeholder response log**
- ...

**Final retrospective**
- What worked: ...
- What did not: ...
- What we would change if we ran this project again: ...

---
