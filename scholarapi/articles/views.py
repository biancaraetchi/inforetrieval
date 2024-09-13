import requests
import csv, re
import os
from django.http import JsonResponse, HttpResponse
from dotenv import load_dotenv
from io import StringIO

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
        for author in json_data["profiles"]:
            authors.append(author["author_id"])
        return authors
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
    try:
        # Get query parameters
        sort = request.GET.get('sort', "")
        self_citation = request.GET.get('self_citation', "")
        authors = request.GET.get('authors', "")

        if not authors:
            return HttpResponse("Error: No authors provided", content_type='text/plain', status=400)

        # Fetch author IDs based on the provided author name
        author_ids = fetch_author_id(authors)
        if not author_ids:
            return HttpResponse("Error: No authors found", content_type='text/plain', status=404)

        citations = 0
        self_citations = 0  # Initialize self_citations count
        all_articles = []

        # Fetch articles for each author ID
        for id in author_ids:
            articles = fetch_articles_for_id(id, sort)

            # Calculate self-citations if requested
            if self_citation:
                self_citations = find_self_citations(articles, authors, id)

            # Process the articles and citations
            for article in articles:
                # Safely get the citation value, defaulting to 0 if it's None
                citation = article.get("cited_by", {}).get("value", 0)

                # Check if the citation is None and set it to 0
                if citation is None:
                    citation = 0  # Handle None by setting it to 0

                citations += citation  # Increment the total citations

                # Add the article to the list of all articles
                all_articles.append({
                    'title': article["title"],
                    'authors': article["authors"],
                    'year': article["year"],
                    'citations': citation
                })

        # Generate CSV output
        buffer = StringIO()
        writer = csv.writer(buffer)

        # Write the CSV header
        writer.writerow(['Title', 'Authors', 'Year', 'Citations'])

        # Write each article's details
        for article in all_articles:
            writer.writerow([article['title'], article['authors'], article['year'], article['citations']])

        # Write total and self-citations
        writer.writerow(["Total citations", str(citations)])
        if self_citation:
            writer.writerow(["Self citations", str(self_citations)])

        csv_data = buffer.getvalue()
        buffer.close()

        # Return the CSV response
        return HttpResponse(csv_data, content_type='text/plain')

    except Exception as e:
        # Catch any exceptions and return them as a plain text error
        return HttpResponse(f"Error: {str(e)}", content_type='text/plain', status=500)
