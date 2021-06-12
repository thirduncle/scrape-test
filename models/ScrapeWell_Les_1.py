import requests
import bs4
from bs4 import BeautifulSoup
import pandas as pd

def go():
    page_url_aldi = "https://www.aldi.com.au/en/groceries/price-reductions/"
    page_sourced = requests.get(page_url_aldi).content
    html_content = BeautifulSoup(page_sourced, "html.parser")
    sale_items_titles = [item.get_text(strip=True) for item in html_content.findAll(class_="box--description--header")]
    sale_item_price = html_content.findAll('div', class_="box--price")
    sale_item_price_list = []
    for s in sale_item_price:
        if len(s.findChildren("span", class_ = "box--value", recursive = False)) == 1:
            # If price is >= $1, it's split into value and decimal part
            bv = s.findChildren("span", class_ = "box--value", recursive = False)[0].get_text()
            print(bv)
            bd = s.findChildren("span", class_="box--decimal", recursive=False)[0].get_text()
            sale_item_price_list.append(bv+bd)
        else:
            pass
            # If price is < $1, it's split into value and c (cents) part
            bv = s.findChildren("span", class_ = "box--value", recursive = False)[0].get_text()
            bd = s.findChildren("span", class_ = "box--value", recursive = False)[1].get_text()
            sale_item_price_list.append(bv+bd)

    return pd.DataFrame({'Sale Items': sale_items_titles, 'Sale Price': sale_item_price_list}).to_html()









