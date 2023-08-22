```python
from bs4 import BeautifulSoup
import requests

def handle_pagination(input_link):
    """
    Function to handle pagination on LinkedIn Sales Navigator
    """
    page_number = 1
    while True:
        url = input_link + "&page=" + str(page_number)
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        pagination = soup.find(id='pagination')

        if not pagination:
            break

        yield url
        page_number += 1
```