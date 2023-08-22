```python
import requests
from bs4 import BeautifulSoup

def access_linkedin(input_link):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    response = requests.get(input_link, headers=headers)

    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        print("Failed to access the LinkedIn Sales Navigator link.")
        return None
```