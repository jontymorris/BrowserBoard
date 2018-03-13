from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse

from home import services, scraper

# GET
def index(request):
	return render(request, 'home/index.html', services.get_current_alerts())

# GET
def edit(request):
	return render(request, 'home/edit.html', services.get_all_alerts())

# GET
def open(request):
	try:
		return redirect('//' + services.view_alert(request.GET.get('id', '')))
	except:
		return HttpResponse('Something went wrong')

# POST
def add(request):
	try:
		url = request.POST.get('url', '')

		# The url is empty
		if not url:
			return JsonResponse( {'error': 'URL cannot be empty'} )

		scraper.initial_scrape(url)

		return JsonResponse( {'error': False} )
	except:
		return JsonResponse( {'error': 'Something went wrong'} )

# POST
def remove(request):
	try:
		alert_id = request.POST.get('id', '')
		services.delete_alert(alert_id)

		return JsonResponse( {'error': False} )
	except:
		return JsonResponse( {'error': 'Something went wrong'} )