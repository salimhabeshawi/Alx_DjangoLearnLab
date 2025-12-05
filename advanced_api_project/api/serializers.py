from rest_framework import serializers
from datetime import datetime
from .models import Author, Book

# Serializer for the Book model.
# Includes custom validation for publication_year.
class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ["id", "title", "publication_year", "author"]
    
     # Custom validation: ensure publication_year is not in the future
    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# Serializer for the Author model.
# Includes nested BookSerializer to serialize related books.
class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["id", "name", "books"]