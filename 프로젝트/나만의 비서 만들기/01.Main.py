import speech_recognition as sr

from MicInput import InMic, OutMic, CrossRoad
from Weather import Weather

r = sr.Recognizer()# 인식을 위한 객체 생성
mic = sr.Microphone()# 마이크 사용을 위한 객체 생성
isTrue = False
result = " "
# while True:
#     result = InMic(r, mic)
#     isTrue = CrossRoad(isTrue, result) 
#     if isTrue:
#         OutMic(r, mic, result)
#         isTrue = False
Weather(37.5894,126.7692)
    