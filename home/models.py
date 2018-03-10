from django.db import models

class Alert(models.Model):
	# Url we are tracking
	tracking_url = models.URLField(max_length=500)
	# Image to be displayed
	img = models.URLField(max_length=500)
	
	# What object should we use when scraping this?
	scraper_object = models.CharField(max_length=100)

	# The link the user will be directed to when clicking the alert
	alert_url = models.URLField(max_length=500)
	# Should this alert be displayed?
	should_display = models.BooleanField(default=False)

	def __str__(self):
		return self.tracking_url