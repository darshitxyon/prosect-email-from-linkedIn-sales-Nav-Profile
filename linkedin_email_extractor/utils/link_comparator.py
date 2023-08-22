```python
def compare_links(scrapy_emails, bs_emails):
    """
    This function compares the emails extracted by Scrapy and BeautifulSoup.
    It creates a union set of the emails to ensure no duplicates.
    """
    # Convert lists to sets for easy comparison
    scrapy_set = set(scrapy_emails)
    bs_set = set(bs_emails)

    # Create a union set of emails
    union_emails = scrapy_set.union(bs_set)

    return list(union_emails)
```