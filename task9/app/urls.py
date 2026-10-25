from django.shortcuts import render
from django.urls import path
from .views import loan

urlpatterns = [
    path('', loan, name='loan'),
]