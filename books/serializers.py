from collections import UserDict, UserList
from rest_framework import serializers 
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=False, max_length=100)
    author = serializers.CharField(requried=False, max_length=100)
    publication_date= serializers.DateField(requried = False)

    class Meta:
        model = Book 
        fields='__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        user = UserDict.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user

    class Meta:
        model = UserList
        fields = ('email', 'password')