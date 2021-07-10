# import requests
# from bs4 import BeautifulSoup

# url = "https://play.google.com/store/movies/top"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.101 Safari/537.36",
#     "Accept-Language":"ko-KR,ko"
#     }

# res = requests.get(url, headers=headers)
# res.raise_for_status()

# soup = BeautifulSoup(res.text, "lxml")

# movies = soup.find_all("div", attrs={"ImZGtf mpg5gc"})
# print(len(movies))

# # with open("movies.html", "w", encoding="utf8") as f:
# #     f.write(soup.prettify()) #html 문서를 예쁘게 출력

# for movie in movies:
#     title = movie.find("div", attrs={"class":"WsMG1c nnK0zc"}).get_text()
#     print(title)


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