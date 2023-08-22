# LinkedIn Sales Navigator Profiles Email Extractor

This is a web scraping tool built with Python, Scrapy, and BeautifulSoup. It extracts all the prospect emails from a LinkedIn Sales Navigator link.

## Features

- Extract all the prospect emails from LinkedIn Sales Navigator link.
- Handle pagination and dynamic content.
- Output all the emails along with some metadata related to that email in a txt file.
- Take input using user input prompt.
- Compare links extracted using Scrapy and BeautifulSoup. Create a Union set for the emails.
- Properly access LinkedIn Sales Navigator links.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python Package Installer)

### Installation

1. Download and install Python from [here](https://www.python.org/downloads/).
2. Clone this repository or download the zip file.
3. Navigate to the project directory in your terminal.
4. Install the required packages using pip:

```bash
pip install -r requirements.txt
```

### Usage

1. Run the main script:

```bash
python main.py
```

2. When prompted, enter the LinkedIn Sales Navigator link.
3. The script will extract all the emails and output them in a txt file.

## User Fillable Variables

In the `main.py` file, you can modify the following variables:

- `input_link`: The LinkedIn Sales Navigator link from where you want to extract emails.
- `output_file`: The name of the txt file where the extracted emails will be stored.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

[MIT](https://choosealicense.com/licenses/mit/)