"""
WSGI config for BrowserBoard project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.0/howto/deployment/wsgi/
"""

import os
import sched, time
from threading import Thread

from django.core.wsgi import get_wsgi_application
from home import scraper

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "BrowserBoard.settings")

def alert_service(timer):
	scraper.routine_scrape()

	# Schedule next update for 30 mins
	timer.enter(60*30, 1, alert_service, (timer,))

def start_services():
	timer = sched.scheduler(time.time, time.sleep)
	timer.enter(0, 1, alert_service, (timer,))
	timer.run()

background_thread = Thread(target=start_services)
background_thread.start()

application = get_wsgi_application()
