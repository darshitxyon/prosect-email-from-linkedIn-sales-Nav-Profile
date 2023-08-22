```python
from bs4 import BeautifulSoup
import requests
from linkedin_email_extractor.utils.pagination_handler import handle_pagination
from linkedin_email_extractor.utils.email_extractor import EmailData

bs_emails = []

def extract_emails_bs(input_link):
    global bs_emails
    bs_emails = []
    session = requests.Session()
    response = session.get(input_link)
    soup = BeautifulSoup(response.text, 'html.parser')
    extract_emails_from_page(soup)
    handle_pagination(soup, session, extract_emails_from_page)

def extract_emails_from_page(soup):
    global bs_emails
    email_elements = soup.find_all(id='email')
    for email_element in email_elements:
        email = email_element.get_text()
        metadata = extract_metadata(email_element)
        email_data = EmailData(email, metadata)
        bs_emails.append(email_data)

def extract_metadata(email_element):
    metadata = {}
    # Add code here to extract metadata related to the email
    return metadata
```