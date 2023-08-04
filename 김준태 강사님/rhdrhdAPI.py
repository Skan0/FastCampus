import requests
import csv
import json

params = {
	'serviceKey': 'yZjCAcvM0IO2PH0loCgAHG8MgMGZDKeRvjANu9jmNg37//gopdhVFEyi996ap5xYdK9ImQqNLQb42cnn59ryOQ==',
	'returnType': 'json',
	'numOfRows': '100',
	'pageNo': '1',
	'sidoName': '서울',
	'ver': '1.0',
}

response = requests.get('http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty', params=params)
print(response.text)
data = json.loads(response.text)
airinfo_list =data['response']['body']['items']

for airinfo in airinfo_list:
    print(airinfo['stationName'],airinfo['sidoName'],airinfo['pm25Value'])

result= [['측정소명','시/도명','미세먼지 수치']]    
with open('airinfo.csv', 'a', encoding = "utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerous(result)