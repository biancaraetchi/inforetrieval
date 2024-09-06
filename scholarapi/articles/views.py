import requests
import csv
import os
from django.http import JsonResponse, HttpResponse
from dotenv import load_dotenv

load_dotenv()

base_url = os.getenv('BASE_URL')
api_key = os.getenv('API_KEY')

# Endpoint to fetch author ids for a particular name
# Should change the API to the Profiles API
def fetch_author_id(request, **kwargs):
    api_url = base_url+"search?engine=google_scholar&q=S%20Benson-Amram&api_key="+api_key
    try:
        response = requests.get(api_url)
        data = response.json()
        return JsonResponse(data)
    except requests.RequestException as e:
        return JsonResponse({'error': 'Failed to fetch data', 'details': str(e)}, status=500)

# Endpoint to fetch + csv the data
# Using a predefined author id for now
def fetch_articles(request):
    # options for sort: either blank or 'pubdate'
    sort = request.GET.get('sort', "")
    api_url = base_url+"search?engine=google_scholar_author&author_id=QlEwuLcAAAAJ&api_key="+api_key+"&sort="+sort
    try:
        response = requests.get(api_url)
        json_data = response.json()
        print(json_data["articles"] )

        # Create a HttpResponse object with CSV header
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="data.csv"'

        # Create a CSV writer object
        writer = csv.writer(response)

        # Write headers (assuming JSON data has a list of dictionaries)
        if json_data:
            articles = json_data["articles"]
            writer.writerow(['Title','Authors','Year','Citations'])

            # Write data rows
            for article in articles:
                writer.writerow([article["title"], article["authors"],article["year"],str(article["cited_by"].get("value"))])

            return response
        else:
            return JsonResponse(json_data)

    except requests.RequestException as e:
        return JsonResponse({'error': 'Failed to fetch data', 'details': str(e)}, status=500)
