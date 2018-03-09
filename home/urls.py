from django.urls import path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('edit', views.edit, name='edit'),
	path('add', views.add, name='add'),
	path('remove', views.remove, name='remove')
]