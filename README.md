# Tech stack
`Python` framework `Django`

# How to run project

* Navigate to `scholarapi`: `cd scholarapi`
* Install requirements: `pip install -r requirements.txt`
* Create `.env` file; copy all variables from `.env_example`, adding your API key
* Run server on `localhost:8000`: `python manage.py runserver`
* Open new terminal and navigate to `pysimplegui` : `cd pysimplegui`
* Install PySimpleGui : `pip install PysimpleGui`
* Run gui : `python gui.py`

# API specifications

* `articles/`: endpoint for retrieving all articles related to the authors

The following parameters are available:
1. `sort`: to sort the articles on the number of citations, leave as blank; to sort them based on the publishing date, set it as "pubdate"
2. `self_citation`: to skip self-citations, leave as blank; to add self-citations, set as "true"
3. `authors`: name of author(s) you would like to retrieve the articles for 

# Screenshots of input/output

* Articles for author `Brian Setz`, sorted based on publishing date, with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/93f39fe6-4e45-410f-a40a-e2c419f675d7)
  ![image](https://github.com/user-attachments/assets/c68fa6d8-74b4-4c8b-9b2e-9751c60b26cb)

* Articles for author `Arnold Meijster`, sorted based on publishing date, with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/3577b3b6-d424-4d99-8732-78cac230e810)
  ![image](https://github.com/user-attachments/assets/7fdf3b12-8f12-4683-80ee-16e870deb384)

* Articles for author `Vasilios Andrikopoulos` with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/133fe42e-2498-410e-b327-375661be3cc4)
  ![image](https://github.com/user-attachments/assets/2c9a8e55-349c-4dc2-864d-3d1d3310dc35)

* Articles for author `Daniel Feitosa`, sorted based on publishing date, with total count of self-citations:
  ![image](https://github.com/user-attachments/assets/af4448df-36d3-4660-b218-538d4f41be7b)
  ![image](https://github.com/user-attachments/assets/04a9d0d2-8b95-4747-91de-1db708240285)

* Articles for author `George Azzopardi`, without total count of self-citations:
  ![image](https://github.com/user-attachments/assets/252803f0-626d-4a03-98f5-2dc763dc65a4)
  ![image](https://github.com/user-attachments/assets/4b11b69f-f1a9-4b31-bcd5-85fbc3bd8f0c)


