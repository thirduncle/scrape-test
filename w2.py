import requests
from urllib.parse import quote, quote_plus

raw_string = 'a query with /, spaces and?&'
url = 'http://www.webscrapingfordatascience.com/paramhttp/?query='

r_quote = requests.get(url + quote(raw_string, safe=''))
r_quote_plus = requests.get(url + quote_plus(raw_string))

"""
print(r_quote.url)
print(r_quote_plus.url)
print(r_quote.text)
print(r_quote_plus.text)
"""

# Using requests only

url_r = 'http://www.webscrapingfordatascience.com/paramhttp/'

parameters = {
    'query' : 'a query with /, spaces and?&'
}

r = requests.get(url_r, params=parameters)

print(r.url)
print(r.text)

