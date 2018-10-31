import re
import requests
url =  'https://www.sonymobile.com/us/products/phones/',\
'https://www.sonymobile.com/cn/products/phones/',\
'https://www.sonymobile.com/in/products/phones/',\
'https://www.sonymobile.com/mx/products/phones/',\
'https://www.sonymobile.com/br/products/phones/',\
'https://www.sonymobile.com/gb/products/phones/',\
'https://www.sonymobile.com/de/products/phones/',\
'https://www.sonymobile.com/fr/products/phones/',\
'https://www.sonymobile.com/es/products/phones/',\
'https://www.sonymobile.com/ru/products/phones/',\
'https://www.sonymobile.com/se/products/phones/',\
'https://www.sonymobile.com/global-en/products/phones/',\
'https://www.sonymobile.com/global-es/products/phones/',\
'https://www.sonymobile.com/global-fr/products/phones/',\
'https://www.sonymobile.com/global-ar/products/phones/',\
'https://www.sonymobile.com/global-zh/products/phones/',\
'https://www.sonymobile.com/id/products/phones/',\
'https://www.sonymobile.com/pt/products/phones/',\
'https://www.sonymobile.com/pl/products/phones/',\
'https://www.sonymobile.com/gr/products/phones/',\
'https://www.sonymobile.com/tr/products/phones/',\
'https://www.sonymobile.com/dk/products/phones/',\
'https://www.sonymobile.com/no/products/phones/',\
'https://www.sonymobile.com/it/products/phones/',\
'https://www.sonymobile.com/nl/products/phones/',\
'https://www.sonymobile.com/il/products/phones/',\
'https://www.sonymobile.com/au/products/phones/',\
'https://www.sonymobile.com/ca-en/products/phones/',\
'https://www.sonymobile.com/ie/products/phones/',\
'https://www.sonymobile.com/my/products/phones/',\
'https://www.sonymobile.com/sg/products/phones/',\
'https://www.sonymobile.com/at/products/phones/',\
'https://www.sonymobile.com/ch-de/products/phones/',\
'https://www.sonymobile.com/ca-fr/products/phones/',\
'https://www.sonymobile.com/ch-fr/products/phones/',\
'https://www.sonymobile.com/hk/products/phones/',\
'https://www.sonymobile.com/ir/products/phones/',\
'https://www.sonymobile.com/sa/products/phones/',\
'https://www.sonymobile.com/tw/products/phones/',\
'https://www.sonymobile.com/vn/products/phones/',\
'https://www.sonymobile.com/ar/products/phones/',\
'https://www.sonymobile.com/eg/products/phones/',\
'https://www.sonymobile.com/iq/products/phones/',\
'https://www.sonymobile.com/ae/products/phones/',\
'https://www.sonymobile.com/ng/products/phones/',\
'https://www.sonymobile.com/za/products/phones/',\
'https://www.sonymobile.com/th/products/phones/',\
'https://www.sonymobile.com/cl/products/phones/',\
'https://www.sonymobile.com/kr/products/phones/',\
'https://www.sonymobile.com/be/products/phones/',\
'https://www.sonymobile.com/cz/products/phones/',\
'https://www.sonymobile.com/fi/products/phones/',\
'https://www.sonymobile.com/hu/products/phones/',\
'https://www.sonymobile.com/ro/products/phones/',\
'https://www.sonymobile.com/ua/products/phones/',\
'https://www.sonymobile.com/bg/products/phones/',\
'https://www.sonymobile.com/be-fr/products/phones/',\
'https://www.sonymobile.com/co/products/phones/',\
'https://www.sonymobile.com/sa-en/products/phones/',\
'https://www.sonymobile.com/ae-en/products/phones/',
#url = 'https://www.sonymobile.com/gb/products/phones/'
for i in url:
    page = requests.get(i)
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(page.text, 'html.parser')
sfsd    for a in soup.find_all(class_='product-name p2', href=True):
        product=(a['href']) + "buy/"
sdfsdfds        page = requests.get(product)
        if page.status_code == 404:
            print(product)

#url2 = "https://www.sonymobile.com/gb/products/phones/xperia-xz2-premium/buy/"
#page = requests.get(url2)
#print (page.status_code)
#
