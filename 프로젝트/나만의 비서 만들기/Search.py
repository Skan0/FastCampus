import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def Search(key):
    driver = webdriver.Chrome()
    driver.get('https://www.naver.com/')
    time.sleep(5)
    WebDriverWait(driver,10).until(EC.presence_of_element_located(By.CSS_SELECTOR, '#query'))
    search_input = driver.find_element(By.CSS_SELECTOR, '#query')
    search_input.send_keys(key)
    search_button = driver.find_element(By.CSS_SELECTOR, '#search-btn')
    search_button.click()
    time.sleep(10)
    driver.quit()