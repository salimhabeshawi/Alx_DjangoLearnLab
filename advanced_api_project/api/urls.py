from django.urls import path
from .views import (
    AuthorListCreateView,
    AuthorDetailView,
    BookListCreateView,
    BookDetailView
)

urlpatterns = [
    path('authors/', AuthorListCreateView.as_view(), name="author-list"),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name="author-detail"),
    path('books/', BookListCreateView.as_view(), name="book-list"),
    path('authors/', BookDetailView.as_view(), name="book-detail"),
]
