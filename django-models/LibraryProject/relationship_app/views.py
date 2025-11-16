from django.contrib.auth.decorators import permission_required, user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.detail import DetailView
from django.contrib.auth import login
from django.urls import reverse_lazy
from .models import Book, Library
from django.views import View
from .forms import BookForm


# Create your views here.
def list_books(request):
    books = Book.objects.all()
    return render(request, "relationship_app/list_books.html", {"books": books})


class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# Login view


class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"
    redirect_authenticated_user = True

# Logout view


class CustomLogoutView(LogoutView):
    pass

# Registration view


def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # login(request, user)
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "relationship_app/register.html", {"form": form})


# helper tests
def is_admin(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'


def is_librarian(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'


def is_member(user):
    return user.is_authenticated and hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

# Admin view (only Admin role)


@user_passes_test(is_admin, login_url='login')
def admin_view(request):
    # prepare context as needed
    context = {'message': 'Welcome, Admin!'}
    return render(request, 'relationship_app/admin_view.html', context)

# Librarian view (only Librarian role)


@user_passes_test(is_librarian, login_url='login')
def librarian_view(request):
    context = {'message': 'Welcome, Librarian!'}
    return render(request, 'relationship_app/librarian_view.html', context)

# Member view (only Member role)


@user_passes_test(is_member, login_url='login')
def member_view(request):
    context = {'message': 'Welcome, Member!'}
    return render(request, 'relationship_app/member_view.html', context)

@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == "POST":
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm()
    return render(request, "relationship_app/add_book.html", {"form": form})

@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect("list_books")
    else:
        form = BookForm(instance=book)
    return render(request, "relationship_app/edit_book.html", {"form": form, "book": book})

@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("list_books")
    return render(request, "relationship_app/delete_book.html", {"book": book})
