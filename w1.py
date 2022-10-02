import requests

url_a = 'https://info-war.gr/infowar-radio/'

url_b = 'http://www.webscrapingfordatascience.com/paramhttp/'

url_c = 'http://www.webscrapingfordatascience.com/paramhttp/?query=a query with spaces'

r = requests.get(url_c)

# Which HTTP status code did we get back from the server?
print(r.status_code)

# What is the textual status code?
print(r.reason)

# What were the HTTP response headers?
print(r.headers)

# The request information is saved as a Python object in r.request:
print(r.request.url)

# What were the HTTP request headers?
print(r.request.headers)

# The HTTP response content:
print(r.text)