from urllib.parse import urlparse

class MangaPanda:

	def __init__(self, soup, site_url, tracking_url, previous_alert_url):
		self.img = soup.find('div', {'id': 'mangaimg'}).img['src']
		self.alert_url = site_url + soup.find('div', {'id': 'latestchapters'}).a['href']