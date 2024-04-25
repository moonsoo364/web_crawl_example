from package import crawl_module as ac
from package import csv_module as sc
from datetime import datetime
import time

def get_current_timestamp():
    current_time = datetime.now()
    timestamp_format = "%Y%m%d_%H%M%S"
    return current_time.strftime(timestamp_format)

def main():
    count = 0
    while True:
        crawlData = ac.crawl_recent_articles()
        if crawlData:
            sc.save_to_csv(crawlData,get_current_timestamp())
            count +=1
        else:
            print("크롤링된 데이터가 없습니다.")
        
    
        print(get_current_timestamp(),':',count,'번째')
        time.sleep(6000)

main()
