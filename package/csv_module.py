import csv

def save_to_csv(data,current_timestamp):
    filename = generate_filename_with_timestamp(current_timestamp)
    fieldnames = ['title', 'link', 'reg_dt']
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(fieldnames)
        for news in data:
            title = news.title
            link = news.link
            regDt = news.regDt
            csv_writer.writerow([title, link,regDt])

def generate_filename_with_timestamp(current_timestamp):
    filename = f"./csv/cnbc_crawl_{current_timestamp}.csv"
    return filename