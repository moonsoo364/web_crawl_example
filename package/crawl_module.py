import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta

class News:
    def __init__(self,title,link,regDt):
        self.title = title
        self.link = link
        self.regDt = regDt
        
def crawl_recent_articles():
    url="https://www.cnbc.com/world/"
    response = requests.get(url)
    crawlData = [];
    if response.status_code == 200:
        soup = BeautifulSoup(response.text,'html.parser')
        ul_element = soup.find('ul','LatestNews-list')
        
        if ul_element:
            for li in ul_element:
                headLine = li.find('a','LatestNews-headline')
                title = headLine.next
                link = headLine.get('href')
                regDt = subtract_minutes_from_current_time(li.find('time').text)
                crawlData.append(News(title,link,regDt))
            return crawlData
    else:
        print("Error With WebPage")
def subtract_minutes_from_current_time(time_string):
    minutes_age = int(time_string.split()[0])
    current_time = datetime.now()
    timestamp_format = "%Y-%m-%d %H:%M:%S"
    new_time = current_time - timedelta(minutes_age)
    return new_time.strftime(timestamp_format)