from home.models import Alert

def get_current_alerts():
	context = dict()
	context['alerts'] = list(Alert.objects.exclude(should_display=False).values("img", "alert_url"))
	
	return context

def get_all_alerts():
	context = dict()
	context['alerts'] = list(Alert.objects.values("img", "alert_url", "id"))

	return context

def delete_alert(id):
	Alert.objects.filter(id=id).delete()