### API E-Utilities for pulling data from PubMed/NCBI databases

import requests
import xml.etree.ElementTree as ET

base_url = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

#### SEARCH FOR ARTICLES MATCHING A QUERY
def search_pubmed(query, max_results = 20):
    params = {
        "db": "pubmed", # tells NCBI E-Utilities API to search for the PubMed database
        "term": query, # actual search query, which can include keywords, boolean operators, and field tags
        "retmax": max_results, # caps the number of results
        "retmode": "json" # requests JSON format
    }
    response = requests.get(f"{base_url}/esearch.fcgi", params=params) # Sends GET request
    return response.json()["esearchresult"]["idlist"] # Parsing the response to extract the list of PubMed IDs (PMIDs) for the articles that match the search query 

#### GET FULL DETAILS FOR A LIST OF PMIDs
def fetch_pubmed_details(pmids_list):
    params = {
        "db": "pubmed",
        "id": ",".join(pmids_list), # Comma-separated list of PMIDs to fetch details for
        "retmode": "xml" # Requests XML format for detailed article information
    }
    response = requests.get(f"{base_url}/efetch.fcgi", params=params) # Sends GET request
    return response.text # Returns the raw XML response containing detailed information about the articles

#### PARSE OUT THE ARTICLE FIELDS WE WANT
def parse_articles(xml_data):
    root = ET.fromstring(xml_data) # Parses the XML data into an ElementTree object
    articles = []

    for article in root.findall(".//PubmedArticle"): # Iterates through each article in the XML
        title = article.findtext(".//ArticleTitle") # Extracts the article title
        pmid = article.findtext(".//PMID") # Extracts the PubMed ID (PMID) for the article

        # Publication date!!
        pub_date = article.find(".//PubDate")
        year = pub_date.findtext("Year") if pub_date is not None else "Unknown" # Extracts publication year, defaults to "Unknown" if not found 
        month = pub_date.findtext("Month") if pub_date is not None else "Unknown" 
        day = pub_date.findtext("Day") if pub_date is not None else "Unknown"

        # Authors!!
        authors = []
        for author in article.findall(".//Author"):
            last_name = author.findtext("LastName") or "Unknown"
            first_name = author.findtext("ForeName") or "Unknown"
            if last_name and first_name:
                authors.append(f"{first_name} {last_name}")

        # MeSH subject terms (health area/topic)!!
        subjects = [
            mesh.findtext("DescriptorName") 
            for mesh in article.findall(".//MeshHeading")
        ]

        # Abstract!!
        abstract = []
        for abstract_text in article.findall(".//AbstractText"):
            label = abstract_text.get("Label")
            text = abstract_text.text or "No abstract available"
            if label:
                abstract.append(f"{label}: {text}")
            else:
                abstract.append(text)
        abstract = "\n".join(abstract) # Joins abstract sections into a single string

        articles.append(
            {"pmid": pmid,
            "title": title,
            "year": year,
            "month": month,
            "day": day,
            "authors": authors,
            "subjects": subjects,
            "abstract": abstract}
        )

    return articles # Returns a list of dictionaries, each containing details about an article

pmids = search_pubmed("diabetes AND treatment", max_results=5) # Example search query
xml_data = fetch_pubmed_details(pmids) # Fetches detailed information for the retrieved PMIDs
articles = parse_articles(xml_data) # Parses the XML data to extract article details

for article in articles:
    print(f"PMID: {article['pmid']}")
    print(f"Title: {article['title']}")
    print(f"Publication Date: {article['year']}-{article['month']}-{article['day']}")
    print(f"Authors: {', '.join(article['authors'])}")
    print(f"Subjects: {', '.join(article['subjects'])}")
    print(f"Abstract: {article['abstract']}\n") 
