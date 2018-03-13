from django.db import models

class Alert(models.Model):
	# The site we are scraping
	site_url = models.URLField(max_length=500)
	
	# Url we are tracking
	tracking_url = models.URLField(max_length=500)
	
	# Image for displaying
	img = models.URLField(max_length=500)
	
	# The link the user will be directed to when clicking the alert
	alert_url = models.URLField(max_length=500)
	
	# Should this alert be displayed on the homepage?
	should_display = models.BooleanField(default=False)

	def __str__(self):
		return self.tracking_url