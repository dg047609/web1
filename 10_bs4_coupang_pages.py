from os import PRIO_PROCESS
import re
import requests
from bs4 import BeautifulSoup

headers = {"User-agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"}

for i in range(1, 6):

    # print("현재 페이지:", i)
    url = "https://www.coupang.com/np/search?q=%EB%85%B8%ED%8A%B8%EB%B6%81&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={0}&rocketAll=false&searchIndexingToken=&backgroundColor=".format(i)

    res = requests.get(url, headers=headers)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    items = soup.find_all("li", attrs={"class":re.compile("^search-product")})
    # print(items[1].find("div", attrs={"class":"name"}).get_text())
    for item in items:

        name = item.find("div", attrs={"class":"name"}).get_text() #상품명

        #애플 제품은 제외
        if "Apple" in name:
            # print("<애플 제품은 제외 하겠습니다.> ")
            continue

        price = item.find("strong", attrs={"class":"price-value"}).get_text() #가격

        #리뷰 100개 이상, 평점 4.5 이상 되는 것만 조회
        
        rate = item.find("em", attrs={"class":"rating"}) #평점
        if rate:
            rate = rate.get_text()
        else:
            # print("<평점 없는 상품은 제외합니다.> ")
            continue
        
        rate_count = item.find("span", attrs={"class":"rating-total-count"}) #평점수
        if rate_count:
            rate_count = rate_count.get_text()[1:-1]
        else:
            # print("<평점 없는 상품은 제외합니다.> ")
            continue

        link = item.find("a", attrs={"class":"search-product-link"})["href"]

        if float(rate) >= 4.5 and int(rate_count) >= 100:
            # print(name, price, rate, rate_count)
            print(f"상품명: {name}")
            print(f"가격: {price}")
            print(f"평점: {rate}점 ({rate_count}개)")
            print("바로가기: {}".format("https://www.coupang.com" + link))
            print("-"*100)

