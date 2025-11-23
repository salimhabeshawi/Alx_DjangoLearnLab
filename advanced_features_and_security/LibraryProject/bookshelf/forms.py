from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year']


class ExampleForm(forms.ModelForm):
    """
    Example form for the Book model.
    This form can be used to create or edit Book instances safely.
    """
    class Meta:
        model = Book
        fields = ['title', 'author', 'library']


class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)
