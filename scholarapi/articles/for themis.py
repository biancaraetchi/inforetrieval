import requests
import csv, re
# from django.http import JsonResponse, HttpResponse
# from dotenv import load_dotenv

# load_dotenv()

# base_url = os.getenv('BASE_URL')
# api_key = os.getenv('API_KEY')

base_url = "https://serpapi.com/"
api_key = "insert api key here"

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

# Endpoint to fetch + csv the data
# Using a predefined author id for now
def fetch_articles(authors):
    # options for sort: either blank or 'pubdate'
    # sort = request.GET.get('sort', "")
    # authors = request.GET.get('authors', "")
    if authors:
        author_ids, citations = fetch_author_id(authors)
        if not author_ids:
            # return JsonResponse({})
            return []
        articles = []
        for id in author_ids:
            api_url = base_url+"search?engine=google_scholar_author&author_id="+id+"&api_key="+api_key
            # +"&sort="+sort
            try:
                response = requests.get(api_url)
                json_data = response.json()
                articles.append(json_data["articles"])
            
            except requests.RequestException as e:
                return []
                # return JsonResponse({'error': 'Failed to fetch data', 'details': str(e)}, status=500)

            # Create a HttpResponse object with CSV header
            # response = HttpResponse(content_type='text/csv')
            # response['Content-Disposition'] = 'attachment; filename="data.csv"'

            # Create a CSV writer object
            # writer = csv.writer(response)

            articles = json_data["articles"]
            # writer.writerow(['Title','Authors','Year','Citations'])
            print('Title,Authors,Year,Citations')

            # Write data rows
            for article in articles:
                citation = article["cited_by"].get("value")
                if citation is None:
                    citation = 0
                # writer.writerow([article["title"], article["authors"],article["year"],str(citation)])
                print(article["title"]+";"+article["authors"]+";"+article["year"]+";"+str(citation))

            
            # writer.writerow(["Total citations;",str(citations)])
            # For Themis
            print("Total citations;",str(citations))
            # return response
    # return JsonResponse({'error': 'No authors provided'}, status=400)
    return []

input1 = input()
input2 = input()
input3 = input()
fetch_articles(input2)
