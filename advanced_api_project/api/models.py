from django.db import models

# Create your models here.

# Author model representing a single author.
# One author can have multiple books (One-to-Many).
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model representing a book written by an author.
# Each Book is linked to one Author via a ForeignKey.
class Book(models.Model):
    title = models.CharField(max_length=100)
    publication_year = models.CharField()
    # Relationship: Many books → One author
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"