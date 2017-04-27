from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	#url(r'^insert-values/$', views.simplexAlgo),
	url(r'^insert-values/$', views.insertValues, name='insertValues'),
	]