from selenium import webdriver
browser = webdriver.Chrome("./chromedriver")
browser.maximize_window() #창 최대화

url = "https://flight.naver.com/flights/"
browser.get(url) #url로 이동

browser.find_element_by_link_text("가는날 선택").click() #가는 날 선택, 클릭


# #이번달 27일, 다음달 28일 선택 
browser.find_elements_by_link_text("27")[0].click() #[0] -> 이번달
browser.find_elements_by_link_text("28")[1].click() #[0] -> 이번달

#제주도 선택 
browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]/div/span").click()

#항공권 검색 클릭
browser.find_element_by_link_text("항공권 검색").click()

#첫번째 결과 출력
elem = browser.find_element_by_xpath("//*[@id='content']/div[2]/div/div[4]/ul/li[1]")
print(elem.text)

