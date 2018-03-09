from home.models import Alert
from urllib.parse import urlparse

sites = {
	"www.mangapanda.com": "MangaPanda",
}

def initial_scrape(url):
	site = urlparse(url).netloc

	if site not in sites:
		raise Exception("That site is not supported")