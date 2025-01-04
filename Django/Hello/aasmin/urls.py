from django.contrib import admin
from django.urls import path
from . import views
from .import Home
from .import contact
from .import Courses


urlpatterns = [
   path('hi/',views.student_list,name="hello_world"),
   path('courses/',Courses.courses,name="Courses"),
   path('home/',Home.home,name="Home"),
   path('contact/',contact.contact,name="Contact")


]