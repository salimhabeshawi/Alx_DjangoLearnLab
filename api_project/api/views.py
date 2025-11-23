# Token Authentication:
# - Clients must send: Authorization: Token <user_token>
# - Tokens are obtained via POST /api/get-token/ using username + password.
# - Permissions:
#   - BookViewSet requires authenticated users for all operations.

from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListAPIView
from .models import Book
from .serializers import BookSerializer

# Create your views here.


class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
