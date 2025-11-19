import requests
from bs4 import BeautifulSoup
import re


class AmazonParser:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def search_product(self, product_name):
        try:
            search_url = f"https://www.amazon.com/s?k={product_name.replace(' ', '+')}"
            response = requests.get(search_url, headers=self.headers)
            soup = BeautifulSoup(response.content, 'html.parser')

            products = []
            items = soup.find_all('div', {'data-component-type': 's-search-result'})

            for item in items[:5]:  # Первые 5 результатов
                product = self.parse_product_item(item)
                if product:
                    products.append(product)

            return products
        except Exception as e:
            print(f"Amazon parser error: {e}")
            return []

    def parse_product_item(self, item):
        try:
            title_elem = item.find('h2')
            price_elem = item.find('span', class_='a-price-whole')
            image_elem = item.find('img', class_='s-image')
            link_elem = item.find('a', class_='a-link-normal')

            if not all([title_elem, price_elem]):
                return None

            title = title_elem.text.strip()
            price_text = price_elem.text.replace(',', '').replace('₹', '').strip()
            price = float(re.sub(r'[^\d.]', '', price_text))
            image_url = image_elem.get('src') if image_elem else ''
            product_url = f"https://amazon.com{link_elem.get('href')}" if link_elem else ''

            return {
                'title': title,
                'price': price,
                'image_url': image_url,
                'url': product_url,
                'marketplace': 'amazon'
            }
        except Exception as e:
            print(f"Error parsing Amazon item: {e}")
            return None