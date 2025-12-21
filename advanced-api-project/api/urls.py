from django.urls import path
from .views import (
    BookListView,
    BookDetailView,
    BookCreateView,
    BookUpdateView,
    BookDeleteView,
)

urlpatterns = [
    path("books/", BookListView.as_view(), name="book-list"),
    path("books/detail/", BookDetailView.as_view(), name="book-detail"),
    path("books/create/", BookCreateView.as_view(), name="book-create"),
    path("books/update/", BookUpdateView.as_view(), name="book-update"),
    path("books/delete/", BookDeleteView.as_view(), name="book-delete"),
]
