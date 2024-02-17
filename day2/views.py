from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'day2/home.html')

def students(request):
    return render(request, 'day2/students.html')

def about(request):
    return render(request, 'day2/about.html')

def create_student(request):
    return render(request, 'day2/create_student.html')

# def delete_student():
#     pass