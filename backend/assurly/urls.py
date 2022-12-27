from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.back_office),
	path('api/create_user', views.create_user),
]