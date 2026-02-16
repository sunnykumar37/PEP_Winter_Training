from django.urls import path
from .views import register_user, contact_view

urlpatterns = [
    path('register/', register_user, name='register'),
    path('contact/', contact_view, name='contact'),
]
