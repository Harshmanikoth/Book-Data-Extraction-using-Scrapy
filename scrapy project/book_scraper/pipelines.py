import re

class BookScraperPipeline:
    RATING_MAP = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5
    }

    def process_item(self, item, spider):
        # 1. Clean Title
        if item.get('title'):
            item['title'] = item['title'].strip()

        # 2. Clean Price
        if item.get('price'):
            price_str = item['price'].strip()
            # Extract numbers and decimal point
            price_match = re.search(r'[\d\.]+', price_str)
            if price_match:
                item['price'] = float(price_match.group())
            else:
                item['price'] = None

        # 3. Clean Availability
        if item.get('availability'):
            avail_str = item['availability'].strip()
            # Normalize availability status
            if "in stock" in avail_str.lower():
                item['availability'] = "In Stock"
            else:
                item['availability'] = "Out of Stock"

        # 4. Clean Rating
        if item.get('rating'):
            rating_str = item['rating'].strip().lower()
            words = rating_str.split()
            rating_val = None
            for word in words:
                if word in self.RATING_MAP:
                    rating_val = self.RATING_MAP[word]
                    break
            item['rating'] = rating_val

        # 5. Clean Product URL
        if item.get('product_url'):
            item['product_url'] = item['product_url'].strip()

        return item
