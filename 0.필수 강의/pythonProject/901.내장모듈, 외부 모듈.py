# 내장 모듈
# :파이썬 설치 시 자동으로 설치되는 모듈

from math import pi,ceil
print(pi)
print(ceil(2.7))
# 반올림 해주는 함수

# 외부 모듈
# : 다른 사람이 만든 파이썬 파일 pip로 설치해서 사용한다
# pyautogui
import pyautogui as pg
pg.moveTo(500,500,duration=2)

