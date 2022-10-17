from bs4 import BeautifulSoup
import requests

url = "https://en.wikipedia.org/wiki/List_of_Romantic_composers"

res = requests.get(url)
soup = BeautifulSoup(res.text,"lxml")
for items in soup.find_all('table',class_="wikitable"):
    for itemss in items.find_all("tr")[1:]:
        e = itemss.find_all('td')
        data = f'{e[0].text.strip()}'
        print(data)
