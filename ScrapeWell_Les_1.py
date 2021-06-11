import requests
import bs4
from bs4 import BeautifulSoup

page_url_aldi = "https://www.aldi.com.au/en/groceries/price-reductions/"

#page_efresh = "https://www.e-fresh.gr/el/proionta?1_and_1=13717&prosfora_=5651&page=1&order=position"

response_code = requests.get(page_url_aldi)

print(response_code)

page_sourced = requests.get(page_url_aldi).content
#page_sourced = requests.get(page_efresh).content

#print(page_sourced)

html_content = BeautifulSoup(page_sourced, "html.parser")

#print(html_content)

#<div class="box--description--header">Berg Short Cut Bacon Rindless 1kg </div> # Aldi sales
#<h3 class="product-name">Αποσμητικό Spray Beauty Finish Dove (2x150 ml) 1+1 Δώρο</h3>
sale_items = html_content.findAll(class_="box--description--header")
#sale_items = html_content.findAll('h3', class_="product-name")

#print(sale_items)

sale_items_titles = [print(i.text.strip()) for i in sale_items]


#print(sale_items_titles)








