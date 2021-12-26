import requests
from parsel import Selector
import time

body_request = {
    "title": "Televisão Full HD",
    "describe": "Uma televisão full hd com vários compatimentos para você experimentar o que há de melhor dos televisores no mercado, uma experiencia incrivel",
    "category": "Televisores",
    "price": 1800,
    "promotion": 1500
}

URL_BASE = "http://books.toscrape.com/catalogue/"
next_page_url = 'page-1.html'
while next_page_url:
    pages = requests.get(URL_BASE + next_page_url)
    items_url = Selector(pages.text).css(".image_container a::attr(href)").getall()
    for item_url in items_url:
        details = requests.get(URL_BASE.replace('catalogue/' + next_page_url, '')  + item_url)
        selector_description = Selector(details.text).css(".product_page p").getall()[3]
    next_page_url = Selector(pages.text).css(".next a::attr(href)").get()





# for _ in range(50):
#     try:
#         request = requests.get("https://www.cloudflare.com/rate-limit-test/", timeout=2)
#     except requests.ReadTimeout:
#         request = requests.get("https://www.cloudflare.com/rate-limit-test/", timeout=2)
#     finally:
#         print(request.status_code)
#         time.sleep(6)