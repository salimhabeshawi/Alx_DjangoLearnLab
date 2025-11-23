from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from .forms import ExampleForm, SearchForm


@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request):
    return HttpResponse("You can view a book.")


@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    return HttpResponse("You can create a book.")


@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request):
    return HttpResponse("You can edit a book.")


@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request):
    return HttpResponse("You can delete a book.")


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# Using Django ORM for safe parameterized queries (prevents SQL injection)


@permission_required('bookshelf.can_view', raise_exception=True)
def book_list(request):
    """
    Secure view: requires 'can_view' permission.
    Lists all books safely.
    """
    books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})


def safe_search(request):
    """
    Secure search using Django ORM.
    Prevents SQL injection by using validated forms and ORM lookups.
    """
    form = SearchForm(request.GET or None)
    results = Book.objects.none()

    if form.is_valid():
        query = form.cleaned_data['query']  # user input is sanitized
        results = Book.objects.filter(
            Q(title__icontains=query) |
            Q(author__icontains=query)
        )

    return render(request, 'bookshelf/book_list.html', {
        'books': results,
        'form': form
    })
