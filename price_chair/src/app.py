__author__ = "Sambasiva Rao Gangineni"

import requests
from bs4 import BeautifulSoup

request = requests.get("https://www.amazon.com/Children-Office-Swivel-Chairs-Adjust/dp/B07BR3R52X/ref=sr_1_1_sspa?ie=UTF8&qid=1541439343&sr=8-1-spons&keywords=study+chairs&psc=1")
content = request.content
soup = BeautifulSoup(content,"html.parser")
element = soup.find("span",{"id":"priceblock_ourprice","class":"a-size-medium a-color-price"},recursive=True)
string_price = element.text.strip()
price = float(string_price[1:])

if price < 60:
    print("Buy the chair")
    print("The current price is {}".format(string_price))
else:
    print("Don't buy the chair")