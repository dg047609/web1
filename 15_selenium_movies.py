import requests
from bs4 import BeautifulSoup

url = "https://play.google.com/store/movies/top?hl=ko&gl=US"
headers = {
    "User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language":"ko-KR,ko"
    }

res = requests.get(url, headers=headers)
res.raise_for_status()

soup = BeautifulSoup(res.text, "lxml")

movies = soup.find_all("div", attrs={"class":"WHE7ib mpg5gc"})
print(len(movies))

with open("movies.html", "w", encoding="utf8") as f:
    f.write(soup.prettify()) #html 문서를 예쁘게 출력