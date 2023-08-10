import speech_recognition as sr
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def InMic(r,mic):
    # 매개변수가 제대로 왔는지 확인, 나중에 tts로 바꾸자    
    if not isinstance(r, sr.Recognizer):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    if not isinstance(mic,sr.Microphone):
        raise TypeError("`recognizer` must be `Recognizer` instance")
    with mic as source: # 마이크에 담긴 소리를 토대로 아래 코드 실행
        #r.adjust_for_ambient_noise(source) # 잡음 제거 코드 (없어도 무방)
        print('인식 중...')
        audio = r.listen(source, timeout=5, phrase_time_limit=5) # 해당 소리를 오디오 파일 형태로 변환
    
    result = r.recognize_google(audio, language = "ko-KR") # 오디오를 토대로 음성 인식
    return result

def OutMic(r, mic, result):         
#print(type(result)) result는 str값이다.
    try:
        print('결과: ' + result) # 인식 결과 출력  
    except sr.UnknownValueError:
        print("음성 인식 실패")
    except sr.RequestError:
        print("서버 에러 발생")
    except sr.WaitTimeoutError:
        print("인식 실패")
        
def CrossRoad(isTrue, result):
    if isTrue:
        pass
        if '시리' in result:
            print("네")
            return True
    elif '검색' in result:
        Search(result)

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
    
#def Weather
#def BrownSmog

    