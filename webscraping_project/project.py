import requests
from bs4 import BeautifulSoup

def scrape_weather():
    print("[오늘의 날씨]")
    url = "https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EC%84%9C%EC%9A%B8+%EB%82%A0%EC%94%A8&oquery=%EB%82%A0%EC%94%A8&tqi=hnKSiwp0Jy0ssUpUS48ssssstXh-335422"
    res = requests.get(url)
    res.raise_for_status()
    soup = BeautifulSoup(res.text, "lxml")

    #맑음, 어제보다 2도 높아요
    cast = soup.find("p", attrs={"class":"cast_txt"}).get_text()
    #현재 온도, 최저, 최고 온도
    curr_temp = soup.find("p", attrs= {"class":"info_temperature"}).get_text().replace("도씨", "")
    min_temp = soup.find("span", attrs={"class":"min"}).get_text()
    max_temp = soup.find("span", attrs={"class":"max"}).get_text()
    #오전, 오후 비올 확률
    morning_rain_rate = soup.find("span", attrs={"class":"point_time morning"}).get_text().strip()
    afternoon_rain_rate = soup.find("span", attrs={"class":"point_time afternoon"}).get_text().strip()

    
    #미세먼지, 초미세먼지
    dust = soup.find("dl", attrs={"class":"indicator"})
    pm10 = dust.find_all("dd")[0].get_text()
    pm25 = dust.find_all("dd")[1].get_text()

    #출력
    print(cast)
    print(" 현재 온도: {0}, 최저 온도: {1}, 최고 온도: {2}".format(curr_temp, min_temp, max_temp))
    print("오전 {0}, 오후 {1}".format(morning_rain_rate, afternoon_rain_rate))
    print()
    print("미세먼지 {}".format(pm10))
    print("초미세먼지 {}".format(pm25))
    print()


def scape_headline_news():
    print("[헤드라인 뉴스]")
    

if __name__ == "__main__":
    scrape_weather() #오늘의 날씨정보 가져오기
    scrape_headline_news()