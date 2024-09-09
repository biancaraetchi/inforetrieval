import PySimpleGUI as sg
import requests


# Function to fetch articles from the backend
def fetch_articles(author_name, sort_by=None, self_citation=None):
    # URL for your backend API
    url = "http://localhost:8000/"

    # Parameters to send to the backend
    params = {
        'authors': author_name,
    }
    if sort_by:
        params['sort'] = sort_by
    if self_citation:
        params['self_citation'] = self_citation

    # Make the GET request to the Django backend
    response = requests.get(url, params=params)

    if response.status_code == 200:
        return response.json()  # Assuming the backend sends a JSON response
    else:
        sg.popup_error(f"Error: {response.status_code}", response.text)
        return []


# Layout for the PySimpleGUI window
layout = [
    [sg.Text('Enter Author Name:'), sg.InputText(key='-AUTHOR-')],
    [sg.Text('Sort By:'), sg.Combo(['', 'pubdate'], key='-SORT-')],
    [sg.Checkbox('Include Self Citations', key='-SELF_CITATION-')],
    [sg.Button('Fetch Articles'), sg.Button('Exit')],
    [sg.Output(size=(80, 20))],  # Output section to display results
]

# Create the window
window = sg.Window('Article', layout)

# Event loop to process "events" and get the values from the inputs
while True:
    event, values = window.read()

    # If user closes the window or presses "Exit", end the program
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # Fetch articles if the user presses "Fetch Articles"
    if event == 'Fetch Articles':
        author_name = values['-AUTHOR-']
        sort_by = values['-SORT-']
        self_citation = values['-SELF_CITATION-']

        if not author_name:
            sg.popup_error('Please enter an author name.')
        else:
            # Call the fetch_articles function
            articles = fetch_articles(author_name, sort_by, self_citation)

            # Clear the output section
            window['-OUTPUT-'].update('')

            # Display the fetched articles in the output section
            if articles:
                for article in articles:
                    print(f"Title: {article['title']}")
                    print(f"Authors: {article['authors']}")
                    print(f"Year: {article['year']}")
                    print(f"Citations: {article.get('citations', 0)}")
                    print("-" * 40)
            else:
                print("No articles found.")

# Close the window
window.close()
