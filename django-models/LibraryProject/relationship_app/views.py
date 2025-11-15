from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views import View
from django.views.generic import DetailView


# Create your views here.
def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, "relationship_app/book_list.html", {"books": books})

class LibraryDetail(DetailView):
    model = Library
    template_name = "relationship_app/library_details.html"
    context_object_name = "library"