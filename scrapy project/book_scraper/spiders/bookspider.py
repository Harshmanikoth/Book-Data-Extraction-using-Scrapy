import scrapy
from book_scraper.items import BookItem

class BookSpider(scrapy.Spider):
    """
    Spider to scrape book details from books.toscrape.com.
    Crawls through all paginated list pages.
    """
    name = "books"
    allowed_domains = ["books.toscrape.com"]
    start_urls = ["https://books.toscrape.com/"]

    def parse(self, response):
        # Loop through each book container
        for book in response.css("article.product_pod"):
            item = BookItem()
            
            # Extract title
            item["title"] = book.css("h3 a::attr(title)").get()
            
            # Extract price
            item["price"] = book.css("p.price_color::text").get()
            
            # Extract availability (normalize spaces in raw HTML text node)
            item["availability"] = book.xpath("normalize-space(.//p[contains(@class, 'availability')])").get()
            
            # Extract rating from class (e.g. 'star-rating Three')
            item["rating"] = book.css("p.star-rating::attr(class)").get()
            
            # Extract and join product URL
            relative_url = book.css("h3 a::attr(href)").get()
            item["product_url"] = response.urljoin(relative_url)
            
            yield item

        # Pagination: Locate "next" page link and crawl it recursively
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
