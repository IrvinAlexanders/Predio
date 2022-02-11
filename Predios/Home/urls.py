from turtle import home
from django.contrib import admin
from django.urls import include, path
from Home.views import inicio


urlpatterns = [
    path('', inicio.as_view(), name='Home'),
]
