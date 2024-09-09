# Tech stack
`Python` framework `Django`

# How to run project

* Navigate to `scholarapi`: `cd scholarapi`
* Install requirements: `pip install -r requirements.txt`
* Create `.env` file; copy all variables from `.env_example`, adding your API key
* Run server on `localhost:8000`: `python manage.py runserver`
* Open new terminal and navigate to `pysimplegui` : `cd pysimplegui`
* install PySimpleGui : `pip install PysimpleGui`
* Run gui : `python gui.py`

# API specifications

* `articles/`: endpoint for retrieving all articles related to the authors

The following parameters are available:
1. `sort`: to sort the articles on the number of citations, leave as blank; to sort them based on the publishing date, set it as "pubdate"
2. `self_citation`: to skip self-citations, leave as blank; to add self-citations, set as "true"
3. `authors`: name of author(s) you would like to retrieve the articles for 

# Screenshots of input/output

* Articles for author `Brian Setz`, sorted based on publishing date, with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/6b239f8d-29c6-4a5a-ae18-9c4eb2411c9d)

* Articles for author `Arnold Meijster`, sorted based on publishing date, with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/cb205503-721c-45e1-b0dd-066414d7f2be)

* Articles for author `Vasilios Andrikopoulos` with total count of self-citations:
  https://github.com/user-attachments/assets/745e8885-0af3-45d2-9b00-3f59edb175d7

* Articles for author `Vasilios Andrikopoulos` without self-citations:
  https://github.com/user-attachments/assets/66f1c5ce-4633-4a27-b22e-a5a03432203b

* Articles for author `Daniel Feitosa`, sorted based on publishing date, with total count of self-citations:
  https://github.com/user-attachments/assets/376c16e3-96ff-484a-8e9c-f7f674f14205

* Articles for author `George Azzopardi`, with total count of self-citations:
  https://github.com/user-attachments/assets/80893fec-115d-4fa9-8010-8b0b64811b79




