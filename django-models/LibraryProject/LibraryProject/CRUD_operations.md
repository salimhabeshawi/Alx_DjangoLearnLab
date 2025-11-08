**CREATE:**
```python
book = Book.objects.creat(title="1984", author="George Orwell", publication_year=1949)
book
# <Book: Book: 1984 by George Orwell (1949)>
```

**RETRIEVE:**
```python
Book.objects.all()
# <QuerySet [<Book: Book: 1984 by George Orwell (1949)>]>
```

**UPDATE:**
```python
book.title = "Nineteen Eighty-Four"
book.save()
Book.objects.all()
# <QuerySet [<Book: Book: Nineteen Eithty-Four by George Orwell (1949)>]>
```

**DELETE:**
```python
book.delete()
# (1, {'bookshelf.Book': 1})
Book.objects.all()
# <QuerySet []>
```
