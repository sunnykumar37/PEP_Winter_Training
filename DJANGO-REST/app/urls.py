from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserCredentialViewSet
router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'credentials', UserCredentialViewSet)

urlpatterns = [
    path('',include(router.urls)),
   
]