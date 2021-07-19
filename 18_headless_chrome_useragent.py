from selenium import webdriver


options = webdriver.ChromeOptions()
options.headless = False
options.add_argument("window-size=1920 * 1080")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36")

browser = webdriver.Chrome("./chromedriver", options=options)
browser.maximize_window()

url = "https://www.whatismybrowser.com/detect/what-is-my-user-agent"
browser.get(url)
#Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)
#AppleWebKit/537.36 (KHTML, like Gecko) 
# Chrome/91.0.4472.114 Safari/537.36
detected_value = browser.find_element_by_id("detected_value")
print(detected_value.text)
browser.quit()