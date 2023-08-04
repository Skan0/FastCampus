import requests
import json

country = {
    "Seoul":(37.566,126.9784),
    "London":(51.5085,-0.1257),
    "New York":(56.25,-5.2833)
}
for i in range(country):
    response = requests.get('https://api.open-meteo.com/v1/forecast?latitude={i[0]}&longitude={i[1]}&current_weather=true')
    data =json.loads(response.text)
    print(data['current_weather']['temperature'])

def get_weather(city):
     response = requests.get('https://api.open-meteo.com/v1/forecast?latitude={country[city][0]}&longitude={country[city][1]}&current_weather=true')


    