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

# Screenshots of input/output

* Articles for author `Brian Setz`, sorted based on publishing date, with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/6b239f8d-29c6-4a5a-ae18-9c4eb2411c9d)

* Articles for author `Arnold Meijster`, sorted based on publishing date, with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/cb205503-721c-45e1-b0dd-066414d7f2be)

* Articles for author `Vasilios Andrikopoulos` with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/a8862397-8374-4bdb-90bd-ae000c9609de)
  ![image](https://github.com/user-attachments/assets/fc019c97-4bad-4eeb-b2d1-bde245ba393a)
  ![image](https://github.com/user-attachments/assets/511501bd-ef8a-41e1-b6c6-62a863e8bd0d)

* Articles for author `Vasilios Andrikopoulos` without self-citations:
  ![image](https://github.com/user-attachments/assets/44249a91-bcff-4bf8-92d6-ae368f809100)
  ![image](https://github.com/user-attachments/assets/f3b1bd48-92e7-4937-be43-80002ed132a2)
  ![image](https://github.com/user-attachments/assets/7f6c70aa-f08b-4bd1-a4a9-be0a0ee9cde5)

* Articles for author `Daniel Feitosa`, sorted based on publishing date, with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/124a6f23-552c-47f8-b250-599676981c7c)
  ![image](https://github.com/user-attachments/assets/510611de-6b62-46a4-9bdc-502ef1dd9b0d)

* Articles for author `George Azzopardi`, with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/0b461ba3-c56b-445c-8799-d08820283c0b)
  ![image](https://github.com/user-attachments/assets/b920f234-9087-43a1-96df-ad65096c88ce)
  ![image](https://github.com/user-attachments/assets/7e754679-5d6e-40aa-bcc9-aea16327fdba)
  ![image](https://github.com/user-attachments/assets/8eb0b4ee-7e2e-4399-9d68-c4ce076faaba)
  ![image](https://github.com/user-attachments/assets/30665fa6-823f-4e8c-aa9d-e4c49aa09e81)



