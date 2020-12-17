

import time

from bs4 import BeautifulSoup
from urllib.request import urlopen
from plyer import notification

# url of the google news source
url = "https://news.google.com/news/rss"

xml_data = urlopen(url).read()
urlopen(url).close()

sp = BeautifulSoup(xml_data, "xml")
news_list = sp.find_all('item')
news_list = news_list[0:11]  # give us news from 0 to 10

for news in news_list:
	notification.notify(
		title="Top Headlines of Today",
		message = news.title.text + "\n Published on: "+ news.pubDate.text,
		timeout = 2)

	time.sleep(10)




