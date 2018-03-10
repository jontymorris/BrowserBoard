from home.models import Alert

def get_current_alerts():
	context = dict()
	context['alerts'] = list(Alert.objects.exclude(should_display=False).values('img', 'id'))
	
	return context

def get_all_alerts():
	context = dict()
	context['alerts'] = list(Alert.objects.values('img', 'id'))

	return context

def delete_alert(id):
	Alert.objects.get(id=id).delete()

def view_alert(id):
	alert = Alert.objects.get(id=id)
	alert.should_display = False
	alert.save()

	return alert.alert_url