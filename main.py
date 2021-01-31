from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://news.ycombinator.com/').text

soup = BeautifulSoup(source, 'lxml')

csv_file = open('hacker_news_scrape.csv', 'w')

csv_writer = csv.writer(csv_file)
csv_writer.writerow(['article'])

title = soup.find_all('title')

for title in soup.find_all('title'):
    headline = title
    print(headline)

article = soup.find_all('tr', class_='athing')
print(article)

print()

csv_writer.writerow([article])

csv_file.close()
