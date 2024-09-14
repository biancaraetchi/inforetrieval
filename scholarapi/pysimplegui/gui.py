import PySimpleGUI as sg
import requests
import csv
from io import StringIO

# Function to fetch articles from the backend
def fetch_articles(author_name, sort_by=None, self_citation=None, response_format='csv'):
    # URL for your backend API
    url = "http://localhost:8000/articles/"

    # Parameters to send to the backend
    params = {
        'authors': author_name,
        'format': response_format  # Request CSV format
    }
    if sort_by:
        params['sort'] = sort_by
    if self_citation:
        params['self_citation'] = 'true'

    # Make the GET request to the Django backend
    response = requests.get(url, params=params)

    if response.status_code == 200:
        if response_format == 'csv':
            # Parse the CSV data
            csv_data = response.text
            return csv_data  # Return the raw CSV data as text
        else:
            sg.popup_error("Unexpected response format")
            return None
    else:
        sg.popup_error(f"Error: {response.status_code}", response.text)
        return None


# Layout for the PySimpleGUI window
layout = [
    [sg.Text('Enter Author Name:'), sg.InputText(key='-AUTHOR-')],
    [sg.Text('Sort By:'), sg.Combo(['', 'pubdate'], key='-SORT-')],
    [sg.Checkbox('Include Self Citations', key='-SELF_CITATION-')],
    [sg.Button('Fetch Articles (Display CSV)'), sg.Button('Exit')],
    [sg.Multiline(size=(80, 20), key='-OUTPUT-')],  # Multiline for displaying output
]

# Create the window
window = sg.Window('Article Search', layout)

# Event loop to process "events" and get the values from the inputs
while True:
    event, values = window.read()

    # If user closes the window or presses "Exit", end the program
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Fetch articles if the user presses "Fetch Articles"
    if event == 'Fetch Articles (Display CSV)':
        author_name = values['-AUTHOR-']
        sort_by = values['-SORT-']
        self_citation = values['-SELF_CITATION-']

        if not author_name:
            sg.popup_error('Please enter an author name.')
        else:
            # Call the fetch_articles function with 'csv' format
            csv_data = fetch_articles(author_name, sort_by, self_citation, response_format='csv')

            if csv_data:
                # Clear the output section
                window['-OUTPUT-'].update('')

                # Parse the CSV data
                csv_reader = csv.reader(StringIO(csv_data))

                # Display the fetched CSV data in the output section
                for row in csv_reader:
                    window['-OUTPUT-'].print(','.join(row))

# Close the window
window.close()
