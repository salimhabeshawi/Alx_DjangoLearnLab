from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 200)
    def __str__(self):
        return self.name 
    
class Book(models.Model):
    title = models.CharField(max_length = 200)
    publication_year = models.IntegerField()
    author = models.ForiegnKey(Author , on_delete = models.CASCADE, related_name = 'books')
    # i have added the related name because i will use it in creating the nested serializer in a clear and concise manner without creating a specific function to the get the books that are related to the author 


