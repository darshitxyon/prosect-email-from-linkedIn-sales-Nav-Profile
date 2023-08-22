```python
import scrapy
from linkedin_email_extractor.utils.pagination_handler import handle_pagination
from linkedin_email_extractor.utils.email_extractor import EmailData

class LinkedInSpider(scrapy.Spider):
    name = 'linkedin_spider'
    allowed_domains = ['linkedin.com']

    def __init__(self, input_link, *args, **kwargs):
        super(LinkedInSpider, self).__init__(*args, **kwargs)
        self.start_urls = [input_link]

    def parse(self, response):
        emails = response.css('#email::text').extract()
        scrapy_emails = [EmailData(email) for email in emails]

        next_page = handle_pagination(response)
        if next_page is not None:
            yield response.follow(next_page, self.parse)

        yield {'scrapy_emails': scrapy_emails}

def extract_emails_scrapy(input_link):
    from scrapy.crawler import CrawlerProcess

    process = CrawlerProcess(settings={
        'FEED_FORMAT': 'json',
        'FEED_URI': 'temp.json'
    })

    process.crawl(LinkedInSpider, input_link=input_link)
    process.start()

    import json
    with open('temp.json', 'r') as f:
        data = json.load(f)

    return data['scrapy_emails']
```