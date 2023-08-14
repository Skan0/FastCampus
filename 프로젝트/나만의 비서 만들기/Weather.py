import requests
import json

def Weather(latitude, longitude):
    url = f'https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current_weather=true&timezone=auto'
    response = requests.get(url)
    json_data = json.loads(response.text)
    print(f"위도: {latitude}, 경도: {longitude}의 온도")
    print(f"{json_data['current_weather']['temperature']}도")
    
# +위도와 경로를 이용해 google 지도로 검색해서 창 띄우기     