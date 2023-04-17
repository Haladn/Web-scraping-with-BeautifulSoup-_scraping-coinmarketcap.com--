from bs4 import BeautifulSoup
import requests

page=requests.get("https://coinmarketcap.com/").text
#print(page.text)
soup=BeautifulSoup(page,"html.parser")
tbody=soup.tbody
trs=tbody.contents
prices={}

for tr in trs[:10]:
    name,price=tr.contents[2:4]
    fixed_name=name.a.p.string
    fixed_price=price.span.string
    prices[fixed_name]=fixed_price

for tr in trs[10:]:
    name=tr.contents[:5]
    fixed_mame=tr.contents[2].find_all("span")[1].string
    fixed_prices=name[3].span
    money=list(fixed_prices.children)[0]+list(fixed_prices.children)[2]
    prices[fixed_mame]=money
print("{:<20}{:>10}".format("names","prices"))
print("-"*30)
for k,v in prices.items():
    print("{:<20}{:>10}".format(k,v))
    print("_"*30)








