Shared Dependencies:

1. **Exported Variables**: 
   - `scrapy_emails`: List of emails extracted by Scrapy
   - `bs_emails`: List of emails extracted by BeautifulSoup
   - `union_emails`: Union set of emails extracted by both scrapers
   - `input_link`: LinkedIn Sales Navigator link provided by the user
   - `output_file`: Text file to store the extracted emails and metadata

2. **Data Schemas**: 
   - `EmailData`: Schema for storing email and related metadata

3. **DOM Element IDs**: 
   - `email`: ID for email elements in LinkedIn Sales Navigator profiles
   - `pagination`: ID for pagination elements on LinkedIn Sales Navigator

4. **Message Names**: 
   - `input_prompt`: Message for prompting user to enter LinkedIn Sales Navigator link
   - `output_message`: Message indicating the completion of email extraction and location of output file

5. **Function Names**: 
   - `extract_emails_scrapy`: Function in `scrapy_scraper.py` to extract emails using Scrapy
   - `extract_emails_bs`: Function in `beautifulsoup_scraper.py` to extract emails using BeautifulSoup
   - `handle_pagination`: Function in `pagination_handler.py` to handle pagination on LinkedIn Sales Navigator
   - `get_user_input`: Function in `input_handler.py` to get user input for LinkedIn Sales Navigator link
   - `write_output`: Function in `output_handler.py` to write extracted emails and metadata to a text file
   - `compare_links`: Function in `link_comparator.py` to compare links extracted by Scrapy and BeautifulSoup and create a union set
   - `access_linkedin`: Function in `access_handler.py` to access LinkedIn Sales Navigator links properly.