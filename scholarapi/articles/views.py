import requests
import csv, re
import os
from django.http import JsonResponse, HttpResponse
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('BASE_URL')
api_key = os.getenv('API_KEY')

# Endpoint to fetch author ids for a particular name
# Should change the API to the Profiles API
def fetch_author_id(author_names):
    author_names = re.sub(r'\s+', '%20', author_names)
    api_url = base_url+"search?engine=google_scholar_profiles&mauthors="+author_names+"&api_key="+api_key
    try:
        response = requests.get(api_url)
        json_data = response.json()
        authors = []
        citations = 0
        for author in json_data["profiles"]:
            authors.append(author["author_id"])
            citations += author["cited_by"]
        return authors, citations
    except:
        return []

def fetch_articles_for_id(author_id, sort):
    articles = []
    api_url = base_url+"search?engine=google_scholar_author&author_id="+author_id+"&api_key="+api_key+"&sort="+sort
    try:
        response = requests.get(api_url)
        json_data = response.json()
        for article in json_data["articles"]:
            articles.append(article)
        while("serpapi_pagination" in json_data):
            response = requests.get(json_data["serpapi_pagination"].get("next")+"&api_key="+api_key+"&sort="+sort)
            json_data = response.json()
            for article in json_data["articles"]:
                articles.append(article)
        
        return articles
    
    except requests.RequestException as e:
        return JsonResponse({'error': 'Failed to fetch data', 'details': str(e)}, status=500)

def self_citation_call(url, citations, author_id):
    response = requests.get(url)
    json_data = response.json()
    if "organic_results" in json_data:
        for result in json_data["organic_results"]:
            if "publication_info" in result and "authors" in result["publication_info"]:
                for author in result["publication_info"].get("authors"):
                    if author["author_id"] == author_id:
                        citations += 1
                        break
    return citations, json_data

def find_self_citations(articles, author_name, author_id):
    citations=0
    num="20"
    for article in articles:
        if "serpapi_link" in article["cited_by"]:
            citations, json_data = self_citation_call(article["cited_by"].get("serpapi_link")+"&api_key="+api_key+"&q=author:"+author_name+"&num="+num, citations, author_id)
            while ("serpapi_pagination" in json_data and "next_link" in json_data["serpapi_pagination"]):
                citations, json_data = self_citation_call(json_data["serpapi_pagination"].get("next_link")+"&api_key="+api_key+"&q=author:"+author_name+"&num="+num, citations, author_id)
    return citations
            

# Endpoint to fetch + csv the data
# Using a predefined author id for now
def fetch_articles(request):
    # options for sort: either blank or 'pubdate'
    sort = request.GET.get('sort', "")
    self_citation = request.GET.get('self_citation', False)
    authors = request.GET.get('authors', "")
    if authors:
        author_ids, citations_new = fetch_author_id(authors)
        if not author_ids:
            return JsonResponse({})
        for id in author_ids:
            articles = fetch_articles_for_id(id, sort)
            if self_citation:
                self_citations = find_self_citations(articles, authors, id)

            # Create a HttpResponse object with CSV header
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="data.csv"'

            # Create a CSV writer object
            writer = csv.writer(response)

            writer.writerow(['Title','Authors','Year','Citations'])

            # Write data rows
            for article in articles:
                citation = article["cited_by"].get("value")
                if citation is None:
                    citation = 0
                writer.writerow([article["title"], article["authors"],article["year"],str(citation)])
            
            writer.writerow(["Total citations;",str(citations_new)])
            if self_citation:
                writer.writerow(["Self citations;",str(self_citations)])

            return response
    return JsonResponse({'error': 'No authors provided'}, status=400)
