import requests
import csv
from bs4 import BeautifulSoup
"""
def crawl_naver(category, date, page):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
    url = f'https://news.naver.com/main/list.naver?mode=LSD&mid=sec&sid1={category}&date={date}&page={page}'
    response = requests.get(headers = headers, url=url)

    # 파싱하기
    soup = BeautifulSoup(response.text, 'html.parser')

    # 원하는 정보 선택하기
    news_list = soup.select('.type06_headline li dl')

    result_list = [('제목','본문일부','신문사','작성시각')]
    for news in news_list:
        try:
            title = news.select('a')[1].text.strip()
        except IndexError:
            title = news.select('a')[0].text.strip()
        writing = news.select('.writing')[0].text
        result_list.append([title, writing])
        content = news.select('.lede')[0].text
        date = news.select('date')[0].text
        result_list.append([title,content,writing,date])
    with open('news.csv','a',encoding ='UTF-8-sig', newline ='')as f:
        writer = csv.writer(f)
        writer.writerows(result_list)
                
crawl_naver(103, 20230101,1)
"""
headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'}
url='https://www.melon.com/chart/index.htm'
response =requests.get(headers = headers, url =url)
    
soup = BeautifulSoup(response.text,'html.parser')
titles =soup.select('.lst50 .rank01 a')
artists = soup.select('.lst50 .rank02 > a')
melon_list = [['제목', '가수']]
for i in range(50):
    melon_list.append([titles[i].text, artists[i].text])
with open('melon_chart.csv','a',encoding = 'UTF-8-sig')as f:
    writer = csv.writer(f)
    writer.writerows(melon_list)

