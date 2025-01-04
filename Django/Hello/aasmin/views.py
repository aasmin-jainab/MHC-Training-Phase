from django.shortcuts import render,get_list_or_404,redirect

from .models import Student
def student_list(request):
    students=Student.objects.all()
    return render(request,'student_list.html',{'std':students})
