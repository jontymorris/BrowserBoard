import sys

from home.scrapers.manga_panda import *

scraper_sites = {
	'mangapanda.com': 'MangaPanda'
}

def get_class(site):
	for keyword in ['https://', 'http://', 'www.']:
		site = site.strip(keyword)

	return getattr(sys.modules['home.scrapers'], scraper_sites[site])