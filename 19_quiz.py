import requests
import time
from bs4 import BeautifulSoup
from selenium import webdriver

interval = 2

options = webdriver.ChromeOptions()
options.headless = True
options.add_argument("window-size=1920 * 1080")


url = "https://www.naver.com/"
browser = webdriver.Chrome(options=options)
# res = requests.get(url)
# res.raise_for_status()


#접속 후 검색창 클릭
browser.get(url)
elem = browser.find_element_by_class_name("input_text")
elem.click()

#검색창에서 "송파 헬리오시티" 검색
browser.find_element_by_class_name("input_text").send_keys("송파 헬리오시티")
time.sleep(interval)

#"검색" 버튼 클릭
btn = browser.find_element_by_id("search_btn")
btn.click()

#스크롤 내리기
browser.execute_script("window.scrollTo(0, 1098)")
browser.find_element_by_class_name("more_icon_inner").click()

time.sleep(interval)

URL = "https://new.land.naver.com/complexes/111515?ms=37.49751,127.107693,17&a=APT:JGC:ABYG&e=RETAIL&articleNo=2118272021"
RES = requests.get(URL)
RES.raise_for_status()


soup = BeautifulSoup(RES.text, "lxml")

# hellio_citys = soup.find("span", attrs={"class":"text"})

while True:
    state_name = browser.find_element_by_class_name("text")
    state_name.click()
    hellio_citys = soup.find("span", attrs={"class":"text"})
    for hellio_city in hellio_citys:
        homeName = hellio_city.find("h4", attrs={"class":"info_title"}).get_text()
        price = hellio_city.find("span", attrs={"class":"price"}).get_text()
        type = hellio_city.find("span",attrs={"class":"type"}).get_text()
        structure = hellio_city.find("td", attrs={"class":"table_td"}).get.text()
        number = 0
        number += 1
        print(f"--------------매물{number}------------")
        print(f"거래: {type}")
        print(f"면적: {structure}")
        print(f"가격: {price}")
        
        if number >= 10:
            break
    browser.quit()

