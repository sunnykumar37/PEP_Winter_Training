from django.contrib import admin
from django.urls import include, path
from polls.views import signup_view, login_view

urlpatterns = [
    path('', include('polls.urls')),
    path('admin/', admin.site.urls),
    path('sign_up/', signup_view, name='sign_up'),
    path('login/', login_view, name='login'),
]
