from django.shortcuts import render

from . import views
from django.http import HttpResponse
def contact(request):
    return HttpResponse("We Are Glad That You Contacted Us.  THANK YOUUU")