# Studio Charter: <project name>

> Filled in live during the **Studio Charter** session in week 3. Every section below is committed in the same commit at the end of that class block. See [Studio Charter (single-session inception)](https://courses.lpcordova.phd/data510/project-framework/charter-inception.html) for the script and time-boxes.

**Owner team:** Addison Gage and Shanti Brodnick

**Owner Product Lead:** Shanti Brodnick

**Peer Stakeholder POs:** Bradely Allen, Mary Krouse, Aaron Perez Sales

**Instructor / Sponsor:** Lucas Cordova (`LucasCordova` on GitHub)

**GitHub repo:** https://github.com/Addie-Shanti-Org/GenderDisparityinResearch/tree/main

**GitHub Projects board:** https://github.com/orgs/Addie-Shanti-Org/projects/3

**Discord category:** `#Project 2: Addison & Shanti`

**Studio Session:** 3

**Studio formed:** 5/25/2026

## Vision
If this project succeeds, we will help improve women's health by helping to eliminate gender gaps in research.


## Mission
Our mission is to identify gaps between the health issues women actually experience and what has been researched. We will do this by gathering data from online communities about what is being discussed and comparing it to what research has been done on women’s health.

## Context

- **Users / affected parties:** Women will benefit from this project. As well as health researchers who are passionate and determined to understand where research is needed. Women are at risk. Women's health is understudied. This leads to underdiagnosis, discrimination, chronic health issues, and misdiagnosis. Medical researchers, clincal trial designers, and public health policy makers can all use the results of this project to better their research and policies which directly impact women.
- **Data sources:**
  
**Clinical Trials**: https://clinicaltrials.gov/data-api/api
- Access through pytrials python library wrapper https://pypi.org/project/pytrials/
- Query for keywords and through different dates

**PubMed**: https://pmc.ncbi.nlm.nih.gov/tools/developers/
- Access through paperscraper python library https://pypi.org/project/paperscraper/
- Query for keywords and through different dates https 

**Reddit API Data**: [https://developers.reddit.com/docs/capabilities/server/reddit-api](https://academictorrents.com/details/3e3f64dee22dc304cdd2546254ca1f8e8ae542b4)
- Due to Reddit's recent restricting access to APIs, we are using this dataset from Academic Torrents.
- This datasets utilized pushshift dumps from 2005 to 2025.
  
- **Constraints:** Scraping may be rate-limited, we may have limited data storage, and we need to do modeling in which we analyze the data outputs, which may require time.
- **Ethics risks:**
  - We plan on using data for a good cause, but if we do it incorrectly we can be misleading and divert attention away from important topics that need to be studied further. 
  - Another ethics consideration is how we will process, store, and use sensitive data collected. We will aim to anonymize data to the best of our ability, leaving out personal information within text or removing the whole data entry if needed. We will carefully analyze the outputs of any modeling we do, making sure no sensitive data is outputted.
  - We are limited to a few sources of data, for both research and discussion. Getting a general sense of “what is being researched” and “what is discussed most” is difficult, and restrained to the data sources we access. In our findings, we will clarify the exact scope in which we are assessing these things.
  - Scraping is another ethical issue- we have to ensure we have permission from websites to scrape their contents. Scraping research papers is another issue, as it borders pirating and can violate publisher permissions.
  - It is also important to noe the disparity of research regarding the intersectionality of race and gender, which is something we are not covering in our analysis. This is a huge area of published health research that is not looked at. Women of color face systemic components including stereotyping, insurance access, and accessible healthcare that all contributes to the imbalance of equity for racial groups within healthcare. Medical literature overall, struggles to report data regarding sex and gender, it struggles even more so with reporting race and ethnicity.[Bierer BE, Meloney LG, Ahmed HR, White SA. Advancing the inclusion of underrepresented women in clinical research. Cell Rep Med. 2022 Mar 7;3(4):100553. doi: 10.1016/j.xcrm.2022.100553. PMID: 35492242; PMCID: PMC9043984] This will be taken into account when doing our analysis and data collection, specifically when collecting data from online forums, although it is not the center of our research. 


## Success criteria by milestone

- **M1, proposal (W4):** We will have the milestone completed the morning of the day it is due. The submission checklist is fully satisfied and the work is doen to the best of our ability. We will understand our research question(s) and our data collection and engineering process. Articulate how our data pipeline will flow from start to end. 
- **M2, data summary (W7):** We will have the milestone completed the morning of the day it is due. The submission checklist is fully satisfied and the work is done to the best of our ability. Data is fully stored in our railway database, it is completely documented, and we have clear next steps for analytics. 
- **M3, poster rough draft (W10):** We will have the milestone completed the morning of the day it is due. The submission checklist is fully satisfied and the work is done to the best of our ability. We are mostly completed with our modeling and analytics and have a poster rough draft.
- **M4, write-up rough draft (W12):** We will have the milestone completed the morning of the day it is due. The submission checklist is fully satisfied and the work is done to the best of our ability. We will have modeling results and analytic results completey finalized. We will have a paper rought draft that can articulate our final pipeline well.
- **M5, final write-up and poster (W14):** We will have the milestone completed the morning of the day it is due. The submission checklist is fully satisfied and the work is done to the best of our ability. We will have a finished project, finished dashboard, beautiful poster, and well-organized paper! 

## Working agreements (internal to owner team)

- **Sync rhythm:** We will have at minimum one standup per week.
- **Code review:** We will review each other's code at the end of the week. 
- **Decision rule:** Consult Peer POs and see what they think. 

## Working agreements (triad with peer POs)

- **Studio Brief due:** Studio Briefs would be due around the time of each milestone, we will communicate dates directly with our peer stakeholders on discord and email.
- **Studio Critique due:** Studio Critiques will be due a varying number of days before the next milestone. We will communicate dates directly with our peer stakeholders on discord and email.
- **Priority conflict resolution:** Owner team integrates briefs in good faith; the instructor arbitrates (as Process Expert) if peer POs and owner team disagree.

## Response SLAs (Service Level Agreements)

A **Service Level Agreement** is a written promise the triad makes about *how fast* each side responds when a specific signal arrives. Every row must have an answer before this Charter is committed. See [Response SLAs](https://courses.lpcordova.phd/data510/project-framework/charter-inception.html#response-slas-service-level-agreements) for the full definition.

| When this signal arrives... | Who responds | By when |
|-----------------------------|--------------|---------|
| Peer PO files a **Studio Brief** (commits to `studio/briefs/...`, links in `#<project>-studio`) | Owner team | Acknowledge in `#<project>-studio` within 24 hours, with a first-pass adopt / defer / decline call for each item. |
| Peer PO files a **Studio Critique** | Owner team | Respond in `#<project>-studio` within 24 hours and capture follow-up items into the backlog. |
| Owner team posts an **Iteration Review** in `README.md` | Both peer POs | Read before filing the next Brief and Critique |
| Owner team flags a **blocker** in `#<project>-blockers` | Instructor, plus any tagged peer PO | Responds by the next Studio Session at the latest; faster if online. |
| Anyone asks a clarifying question in `#<project>-general` | Whoever is tagged (default: owner team) | Reply within 48 hours, even if the reply is "we will look at this next iteration". |

## Definition of Ready (PBI)

A PBI is ready to be pulled out of `Backlog` and moved into `Create` when it has:

- A one-sentence hypothesis or user story.
- A named **Create**, **Observe**, **Analyze** triple.
- A milestone tag (`M1-proposal`, `M2-data-summary`, `M3-poster-draft`, `M4-writeup-draft`, `M5-final`, `infra`, `ethics`).
- Effort (XS, S, M, L, XL) is clearly labeled
- WIP slack on the board: `Create + Observe + Analyze` is below the team's WIP cap (owners + 1).

## Definition of Done (PBI)

A PBI is done, and may be moved from `Analyze` into `Done`, when:

- The Create artifact is in the repo or linked from the issue.
- The Observe results are recorded somewhere referenceable (notebook output, processed dataset, draft results section).
- The Analyze writeup names a next step (continue, pivot, kill, or decompose into new PBIs).
- A peer PO has either signed off in `#<project>-studio` or filed a Studio Critique covering it.
- The card is linked under *Completed PBIs* in the next Iteration Review in `README.md`.

## Stakeholder alignment memo (one-page summary)

### Why we exist
We exist because we want to help improve women's health by eliminating gender gaps in research. This will be done by identifying the missingness in what is published in medical research and what women talk about online. 

### What we will deliver to peer POs every milestone
- An Iteration Review in this `README.md` by the next milestone
- A summary of which Studio Brief items we adopted, deferred, or declined, and why

### What we need from peer POs every milestone
- A Studio Brief around next class (next iteration's requirements, questions, risks)
- A Studio Critique around 1-3 days before next class (assessment of last week's delivery)

### How to reach us
- Discord category: `#<project>-general` (day-to-day), `#<project>-studio` (Briefs and Critiques), `#<project>-blockers` (impediments)
- GitHub repo: https://github.com/Addie-Shanti-Org/GenderDisparityinResearch
- GitHub Projects board: https://github.com/orgs/Addie-Shanti-Org/projects/3
