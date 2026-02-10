from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {'name': ' Sunny'})

def jinja_view(request):
    return render(request, 'dashboard.jinja', {'name': ' Sunny'})