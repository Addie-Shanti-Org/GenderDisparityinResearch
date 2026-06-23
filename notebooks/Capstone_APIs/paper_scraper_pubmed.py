# Paper scraper for PubMed using E-utilities API
'''
# Paper scraper is used for pulling data from PubMed, which is a database of biomedical literature. The E-utilities API allows us to search for articles, retrieve details about specific articles, and parse the information we need.
'''
import numpy as np
import pandas as pd

# pip install paperscraper
from paperscraper.pubmed import get_pubmed_papers as get_pubmed
#from paperscraper.pubmed import get_query_from_keywords_and_date
from paperscraper.get_dumps import biorxiv, medrxiv, chemrxiv

# Example usage
endo_papers = get_pubmed(query="endometriosis", max_results=10)

'''
endo_paper_two_days = get_query_from_keywords_and_date(
    keywords=[],
    start_date="2024/01/01",
    end_date="2024/01/03")

papers_two_days = get_pubmed(query=endo_paper_two_days, max_results=10)
'''

# Filter query by date to try and get all papers created between Jan 1 and Jan 3, 2024
date_query = '("2024/01/01"[Date - Create] : "2024/01/03"[Date - Create])'
# The cap for max results is 9998
all_papers_two_days = get_pubmed(query=date_query, max_results=9998)
#print(all_papers_two_days)

#test_df = pd.DataFrame.from_records(all_papers_two_days[1:], all_papers_two_days[0])
#print(test_df)







