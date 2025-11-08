from relationship_app.models import Author, Book, Library, Librarian
from django.conf import settings
import django
import os
import sys

# Ensure the Django project root is on sys.path so local apps can be imported
# project root: .../LibraryProject (where manage.py lives)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

# Configure Django settings and initialize Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
if not settings.configured:
    django.setup()


try:
    author = Author.objects.get(name="Salim Ahmed")
    books_by_author = author.book.all()
    print("Books by Salim Ahmed:")
    for book in books_by_author:
        print(f"- {book.title}")
except Author.DoesNotExist:
    print(f"No author found with name Salim Ahmed")

library_name = "Central Library"
try:
    library = Library.objects.get(name=library_name)
    books_in_library = library.books.all()
    print(f"Books in {library_name}:")
    for book in books_in_library:
        print(f"- {book.title} by {book.author.name}")
except Library.DoesNotExist:
    print(f"No library found with name {library_name}")

try:
    librarian = Librarian.objects.get(library__name=library_name)
    print(f"Librarian of {library_name}: {librarian.name}")
except Librarian.DoesNotExist:
    print(f"No librarian found for library {library_name}")
