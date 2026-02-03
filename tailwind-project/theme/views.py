from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'base.html')


def custom_404(request, exception):
    return render(request, '404.html', status= 404)