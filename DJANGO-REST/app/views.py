from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Book, UserCredential
from .serializers import BookSerializer, UserCredentialSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


# ViewSet for UserCredential
class UserCredentialViewSet(viewsets.ModelViewSet):
    queryset = UserCredential.objects.all()
    serializer_class = UserCredentialSerializer