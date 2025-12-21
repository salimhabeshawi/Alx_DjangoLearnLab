from rest_framework import serializers
from .models import Author 
from .models import Book
from datetime import datetime


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("publication date can't be greater than current year ")
        return value
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)
    
    class Meta:
        model = Author 
        fields = ['name', 'books']
""" so i have created a nested serializer to send the data about the author and also about the books that that author is associated with """
