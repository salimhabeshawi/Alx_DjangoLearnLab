from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        # add any other fields you want
        fields = ['title', 'author', 'library']
