from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return render(request, 'home/index.html')

def edit(request):
	return render(request, 'home/edit.html')