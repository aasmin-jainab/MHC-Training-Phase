from django.shortcuts import render

from . import views
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

def courses(request):
    # Define the list of courses
    course_list = [
        "Artificial Intelligence",
        "Data Science",
        "Machine Learning",  # You can add more courses if needed
    ]
    
    # Generate the response with numbering and line breaks
    response = "We offer the best courses:<br>"
    response += "<br>".join(f"{i+1}. {course}" for i, course in enumerate(course_list))
    
    return HttpResponse(response)
