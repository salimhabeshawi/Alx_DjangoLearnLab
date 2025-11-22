from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponse
from .models import Book


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
