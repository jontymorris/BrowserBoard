from urllib.parse import urlparse, urljoin
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

from home.models import Alert
from home.scrapers import *

def get_html(url):
	return urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'})).read()

def initial_scrape(tracking_url):
	site_url = urlparse(tracking_url).netloc
	
	if site_url not in scraper_sites:
		raise Exception('That site is not supported')
	
	soup = BeautifulSoup(get_html(tracking_url), 'html.parser')
	scraper = get_class(site_url)(soup, site_url, tracking_url, '')

	new_alert = Alert(site_url=site_url, tracking_url=tracking_url, img=scraper.img, alert_url=scraper.alert_url, should_display=True)
	new_alert.save()

def routine_scrape():
	for alert in Alert.objects.all():
		soup = BeautifulSoup(get_html(alert.tracking_url), 'html.parser')
		scraper = get_class(alert.site_url)(soup, alert.site_url, alert.tracking_url, alert.alert_url)

		alert.should_display = (scraper.alert_url != alert.alert_url)
		alert.img = scraper.img
		alert.alert_url = scraper.alert_url

		alert.save()