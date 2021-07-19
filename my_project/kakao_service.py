import requests
from bs4 import BeautifulSoup

url = "https://www.kakaocorp.com/page/service/service"
res = requests.get(url)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")
service = soup.find("strong", attrs={"class":"tit_card"})
print(service)
