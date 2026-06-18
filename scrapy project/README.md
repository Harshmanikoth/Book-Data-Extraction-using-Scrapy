# Book Data Extraction using Scrapy

A production-ready, highly optimized web crawling and scraping project built with the **Scrapy** framework to extract book data from [Books to Scrape](https://books.toscrape.com/). This repository demonstrates modern web scraping best practices including pagination handling, data pipeline cleaning, and feed exports.

## Project Overview
This project crawls all 50 pages of the target bookstore website to harvest data for 1,000 books. The extracted raw data undergoes cleaning in custom pipelines (e.g., parsing prices into floats, converting text-based star ratings to integers) and is automatically exported into structured CSV and JSON formats.

## Features
- **Full Site Pagination**: Automatically locates and crawls through all 50 listing pages.
- **Robust Selectors**: Uses clean CSS and XPath selectors to parse metadata safely.
- **Data Normalization Pipeline**: 
  - Converts text ratings (e.g., "Three") to integer values (`3`).
  - Cleans price formats (e.g., "£51.77" to float `51.77`).
  - Normalizes availability statuses (e.g., "In stock" to "In Stock").
  - Resolves relative URLs to absolute URLs.
- **Polite Crawling**: Employs Scrapy's `AutoThrottle` extension to dynamically throttle request rates based on target server load and latencies.
- **Automated Feed Exports**: Configured to export data directly to both `books.csv` and `books.json` simultaneously upon running the spider.

## Tech Stack
- **Language**: Python 3.9+
- **Framework**: Scrapy 2.11+
- **Asynchronous Networking**: Twisted

## Project Structure
```text
scrapy-project/
├── book_scraper/                  # Root project package
│   ├── spiders/                   # Spider module directory
│   │   ├── __init__.py
│   │   └── bookspider.py          # Primary book crawler spider
│   ├── __init__.py
│   ├── items.py                   # Data schemas and definitions
│   ├── pipelines.py               # Data cleaning and transformations
│   └── settings.py                # Scrapy runtime configurations
├── .gitignore                     # Git ignore file
├── README.md                      # Documentation
├── scrapy.cfg                     # Project deployment configuration
└── requirements.txt               # Project dependencies
```

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/book-data-extraction-scrapy.git
   cd book-data-extraction-scrapy
   ```
2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```
3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions
To start the crawling process and generate the output files, run the following command from the project root directory:
```bash
scrapy crawl books
```
Once execution is complete, the project will generate two files in the root folder:
- `books.csv`: Data in comma-separated values format.
- `books.json`: Data in structured JSON array format.

## Sample Output

### CSV Sample (`books.csv`)
```csv
availability,price,product_url,rating,title
In Stock,51.77,https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html,3,A Light in the Attic
In Stock,53.74,https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html,1,Tipping the Velvet
In Stock,50.1,https://books.toscrape.com/catalogue/soumission_998/index.html,1,Soumission
```

### JSON Sample (`books.json`)
```json
[
    {
        "title": "A Light in the Attic",
        "price": 51.77,
        "availability": "In Stock",
        "rating": 3,
        "product_url": "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
    },
    {
        "title": "Tipping the Velvet",
        "price": 53.74,
        "availability": "In Stock",
        "rating": 1,
        "product_url": "https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html"
    }
]
```

## Future Improvements
- **Database Integration**: Implement pipelines to store scraped books in SQLite or PostgreSQL.
- **Proxy Rotation**: Integrate proxy rotation middleware to bypass rate limits on larger scale crawls.
- **User-Agent Rotation**: Utilize `scrapy-user-agents` to randomize requests.
- **Containerization**: Add a `Dockerfile` for easy container deployment.

## Author
- **Your Name** - [GitHub](https://github.com/yourusername) | [LinkedIn](https://linkedin.com/in/yourprofile)
