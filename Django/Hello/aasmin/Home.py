from django.shortcuts import render

from . import views
from django.http import HttpResponse
def home(request):
    return HttpResponse("Welcome To Our Home Page")