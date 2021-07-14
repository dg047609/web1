from os import times
from selenium import webdriver
browser = webdriver.Chrome("./chromedriver")
browser.maximize_window()

#페이지 이동
url = "https://play.google.com/store/movies/top"
browser.get(url)

#지정한 위치로 스크롤 내리기
#모니터 해상도 만큼 1080 위치로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, 1080)") #스크롤 내리기
# browser.execute_script("window.scrollTo(0, 2080)") #스크롤 내리기

#화면 가장 아래로 스크롤 내리기
# browser.execute_script("window.scrollTo(0, document.body.scrollToHeight)")

import time
interval = 2 #2초에 한번씩 스크롤 내림

#현재 문서 높이를 가져와서 저장
previous_height = browser.execute_script("return document.body.scrollHeight") 

#반복 수행
# 스크롤 아래로 내리기
while True:
    #스크롤을 가장 아래로 내림
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight)") 

    #페이지 로딩
    time.sleep(interval) 
    
    #현재 문서 높이를 가져와서 저장
    current_height = browser.execute_script("return document.body.scrollHeight")
    if current_height == previous_height:
        break 

    previous_height = current_height

print("스크롤 완료")

import requests
from bs4 import BeautifulSoup

soup = BeautifulSoup(browser.page_source, "lxml")

movies = soup.find_all("div", attrs={"class":"Vpfmgd"})
# print(len(movies))

for movie in movies:
    title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
    # print(title)

    #할인 전 가격
    original_price = movie.find("span", attrs={"class":"SUZt4c djCuy"})
    if original_price:
        original_price = original_price.get_text()
    else:
        # print(title)
        continue

    #할인 된 가격
    price = movie.find("span", attrs={"class":"VfPpfd ZdBevf i5DZme"}).get_text()

    #링크
    link = movie.find("a", attrs={"class":"JC71ub"})["href"]

    #https://play.google.com + link

    print(f"제목: {title}")
    print(f"할인 전 금액: {original_price}")
    print(f"할인 후 금액: {price}")
    print("링크: ", "https://play.google.com" + link)
    print("-"*100)

browser.quit() #브라우저 종료