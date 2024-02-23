import requests
from bs4 import BeautifulSoup
import pandas as pd

# URL of the page you want to scrape
url = 'https://fbref.com/en/matches/01e57bf5/Chelsea-Tottenham-Hotspur-August-14-2022-Premier-League'

# create comment for scrape table function
def scrape_table(url, table_id, headers):
    # Send an HTTP GET request to the URL
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find the table containing the shots data
    table = soup.find('table', {'id': table_id})

    # Extract the data rows
    data_rows = table.select('tbody tr')

    # Extract the data from each row
    data = []
    for row in data_rows:
        th_element = row.find('th', {'scope': 'row'})
        td_elements = row.find_all('td')

        row_data = [th_element.text] + [td.text for td in td_elements]
        data.append(row_data)

    # Print the headers
    df = pd.DataFrame(data, columns=headers)
    return df

headers = ['Minute', 'Player', 'Squad', 'xG', 'PSxG', 'Outcome', 'Distance', 
           'Body Part', 'Notes', 'SCA 1 Player', 'SCA 1 Event', 'SCA 2 Player', 'SCA 2 Event']


df = scrape_table(url, 'shots_all', headers=headers)

print(df.head())


