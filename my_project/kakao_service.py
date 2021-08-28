import requests
from bs4 import BeautifulSoup

url = "https://www.kakaocorp.com/page/service/service"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
services = soup.find("strong", attrs={"class": "link_item"})
service = services.get_text()
print(service)
