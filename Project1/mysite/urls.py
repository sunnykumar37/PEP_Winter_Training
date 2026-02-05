from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('', include('polls.urls')),
    #path('polls', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('register', views.register, name='register'),
    path('login', views.login_view, name='login'),
]
