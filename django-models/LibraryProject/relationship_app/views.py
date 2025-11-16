from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Book, Library
from django.views import View
from django.views.generic.detail import DetailView


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
