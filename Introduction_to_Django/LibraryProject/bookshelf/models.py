from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(200)
    author = models.CharField(100)
    publication_year = models.IntegerField()
