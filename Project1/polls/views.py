from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import user

def index(request):
    myusers = user.objects.all().values()
    template = loader.get_template('user_list.html')
    context = {
        'myusers': myusers,
    }
    return HttpResponse(template.render(context, request))
