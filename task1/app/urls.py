from django.shortcuts import render
from django.urls import path
from .views import result

urlpatterns = [
    path('', result, name='result'),
]