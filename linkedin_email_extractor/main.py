```python
from scrapers.scrapy_scraper import extract_emails_scrapy
from scrapers.beautifulsoup_scraper import extract_emails_bs
from utils.pagination_handler import handle_pagination
from utils.input_handler import get_user_input
from utils.output_handler import write_output
from utils.link_comparator import compare_links
from utils.access_handler import access_linkedin

def main():
    # Get user input for LinkedIn Sales Navigator link
    input_link = get_user_input()

    # Access the LinkedIn Sales Navigator link
    access_linkedin(input_link)

    # Handle pagination on LinkedIn Sales Navigator
    handle_pagination(input_link)

    # Extract emails using Scrapy
    scrapy_emails = extract_emails_scrapy(input_link)

    # Extract emails using BeautifulSoup
    bs_emails = extract_emails_bs(input_link)

    # Compare links extracted by Scrapy and BeautifulSoup and create a union set
    union_emails = compare_links(scrapy_emails, bs_emails)

    # Write extracted emails and metadata to a text file
    write_output(union_emails)

if __name__ == "__main__":
    main()
```