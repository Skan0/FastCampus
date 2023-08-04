from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By
import time

# 셀레닝엄이 작동할 때 크롬이라는 웹브라우저를 사용
driver = webdriver.Chrome()
driver.get('https://www.melon.com/chart/month/index.htm')
time.sleep(5)

search_button =driver.find_element(By.CSS_SELECTOR,'#conts > div.calendar_prid > div > button')
search_button.click()

for i in range (1,7):
    month_element = driver.find_element(By.CSS_SELECTOR, f"#conts > div.calendar_prid > div > div > dl > dd.month_calendar > ul > li:nth-child({i}) > a")
    month_element.click()
    time.sleep(1)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    titles = soup.select('.lst50 .rank01 a')
    artists = soup.select('.lst50 .rank02 a')
    for i in range(50):
        print(f'{titles[i].text} - {artists[i].text}')

driver.quit()


# request 모듈을 써서 웹 주소에 요청을 보내고, 응답으로 HTML을 받아옴
# 그 HTML을 beautiful soup모듈을  써서 파싱 
#
