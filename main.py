import csv
import requests
from bs4 import BeautifulSoup


URL = 'https://www.bilibili.com/v/popular/rank/knowledge'


# 发起网络请求
response = requests.get(URL)
html_text = response.text
soup = BeautifulSoup(html_text, 'html.parser')

class Video:
    def __init__(self, title, up_name, url):
        self.title = title
        self.up_name = up_name
        # self.up_id = up_id
        self.url = url

    def to_csv(self):
        return [self.title, self.up_name, self.url]

    @staticmethod
    def csv_title():
        return ['Title', 'Author', 'URL']


# 提取列表
items = soup.findAll('li', {'class': 'rank-item'})
videos = []

for itm in items:
    # title = itm.find('a', {'class': 'title'}).text
    # score = itm.find('div', {'class': 'pts'}).find('div').text
    # rank = itm.find('div', {'class': 'num'}).text
    # up_name = itm.find('span', {'class': 'data-box'}).text
    title = itm.find_all('a')[1].text
    up_name = itm.find_all('a')[2].text
    # up_id = itm.find_all('a')[2].get('href')[len('//space.bilibili.com/'):]
    url = itm.find('a', {'class': 'title'}).get('href')

    v = Video(title, up_name, url)
    videos.append(v)

file_name = 'courses.csv'
with open(file_name, 'w', newline='') as f:
    pen = csv.writer(f)
    pen.writerow(Video.csv_title())

    for video in videos:
        pen.writerow(video.to_csv())





