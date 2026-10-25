from django.shortcuts import render
from django.urls import path
from .views import hotels

urlpatterns = [
    path('', hotels, name='hotels'),
]