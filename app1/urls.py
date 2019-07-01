from django.urls import path
from . import views

urlpatterns = [
	path('', views.home),
	path('add', views.result),
    path('index', views.index),
]
