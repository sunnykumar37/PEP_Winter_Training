from rest_framework import serializers
from .models import Book, UserCredential
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'publish_date']


# Serializer for UserCredential
class UserCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredential
        fields = ['id', 'username', 'password']