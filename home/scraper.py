from home.models import Alert

from urllib.parse import urlparse, urljoin
from urllib.request import Request, urlopen

import sys

from bs4 import BeautifulSoup

scraper_objects = {
	'www.mangapanda.com': 'MangaPanda'
}

def str_to_class(str):
    return getattr(sys.modules[__name__], str)

def get_html(url):
	return urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()

def initial_scrape(url):
	site = urlparse(url).netloc

	if site not in scraper_objects:
		raise Exception('That site is not supported')

	soup = BeautifulSoup(get_html(url), 'html.parser')

	scraper_name = scraper_objects[site]
	scraper = str_to_class(scraper_name)(soup, url, '')

	alert = Alert(tracking_url=url, img=scraper.img, scraper_object=scraper_name, alert_url=scraper.alert_url, should_display=True)
	alert.save()


class MangaPanda:

	def __init__(self, soup, url, previous_alert_url):
		self.tracking_url = url
		self.img = soup.find('div', {'id': 'mangaimg'}).img['src']
		
		base_url = urlparse(url).netloc
		self.alert_url = base_url + soup.find('div', {'id': 'latestchapters'}).a['href']
		
		self.should_display = (not self.alert_url == previous_alert_url)