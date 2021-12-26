import requests
import re
from parsel import Selector


# http = requests.get('https://httpbin.org/encoding/utf8')
# seletor = Selector(http.text)

git = requests.get('https://api.github.com/users')
array = git.json()
for user in array:
    print(f"{user['login']} - {user['url']}")