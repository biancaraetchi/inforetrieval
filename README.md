# How to run project

Navigate to `scholarapi`: `cd scholarapi`
Install requirements: `pip install -r requirements.txt`
Create `.env` file; copy all variables from `.env_example`, adding your API key
Run server on `localhost:8000`: `python manage.py runserver`

# API specifications

* `articles/`: endpoint for retrieving all articles related to the authors'

The following parameters are available:
1. `sort`: to sort the articles on the number of citations, leave as blank; to sort them based on the publishing date, set it as "pubdate"
2. `self_citation`: to skip self-citations, leave as blank; to add self-citations, set as "true"
3. `authors`: name of author(s) you would like to retrieve the articles for 
