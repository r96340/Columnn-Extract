from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_cakes"

res = requests.get(url)
soup = BeautifulSoup(res.text,"lxml")
for items in soup.find(class_="wikitable").find_all("tr")[1:]:
    e = items.find_all('td')
    data = f'{e[0].text.strip()}'
    print(data)