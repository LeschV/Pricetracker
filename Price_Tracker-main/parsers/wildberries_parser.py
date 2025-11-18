import requests
import re


class WildberriesParser:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

    def search_product(self, product_name):
        try:
            search_url = f"https://search.wb.ru/exactmatch/ru/common/v4/search"
            params = {
                'query': product_name,
                'resultset': 'catalog',
                'sort': 'popular',
                'limit': 5
            }

            response = requests.get(search_url, headers=self.headers, params=params)
            data = response.json()

            products = []
            for item in data.get('data', {}).get('products', [])[:5]:
                product = self.parse_product_item(item)
                if product:
                    products.append(product)

            return products
        except Exception as e:
            print(f"Wildberries parser error: {e}")
            return []

    def parse_product_item(self, item):
        try:
            title = item.get('name', '')
            price = item.get('salePriceU', 0) / 100  # Цена в рублях
            image_url = f"https://images.wbstatic.net/c246x328/new/{item.get('id', 0)}-1.jpg"
            product_url = f"https://www.wildberries.ru/catalog/{item.get('id', 0)}/detail.aspx"

            return {
                'title': title,
                'price': price,
                'image_url': image_url,
                'url': product_url,
                'marketplace': 'wildberries'
            }
        except Exception as e:
            print(f"Error parsing Wildberries item: {e}")
            return None