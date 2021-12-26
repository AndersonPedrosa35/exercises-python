import requests
from parsel import Selector


request = requests.get('https://httpbin.org/encoding/utf8')
seletor = Selector(request.text)
print(request.content)