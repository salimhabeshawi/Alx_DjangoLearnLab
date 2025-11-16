from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseForbidden
from .models import Book, Library
from django.views import View
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test, login_required


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
