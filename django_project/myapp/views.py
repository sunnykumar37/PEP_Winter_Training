from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse("Hello, world. You're at the myapp index.")
    return render(request, 'index.html')

def contact(request):
    return HttpResponse("This is the contact page of the myapp app.")

def about(request):
    return HttpResponse("This is the about page of the myapp app.")

def projects(request):
    return HttpResponse("This is the Projects page of the myapp app.")

def resume(request):
    return HttpResponse("This is the Resume page of the myapp app.")