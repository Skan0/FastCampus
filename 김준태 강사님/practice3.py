import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://www.melon.com/chart/month/index.htm')

selector = driver.find_elment(By.CSS_SELECTOR,'#conts > div.calendar_prid > div > button')
selector.click()

time.sleep(1)
for i in range(1,7):
    month =driver.find_element(By.CSS_SELECTOR,f"#conts > div.calendar_prid > div > div > dl > dd.month_calendar > ul > li:nth-child({i}) > a")
    month.click()

    time.sleep(1)

    html = driver.page_source
    soup=BeautifulSoup(html,'html.parser')
    titles = soup.select(".lst50 .rank01 a")
    artists =soup.select('.lst50 .rank02 > a')
    for i in range(50):
        print(f'{titles[i].text} - {artists[i].text}')
        