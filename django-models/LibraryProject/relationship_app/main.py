"""Small helper script for relationship_app.

This file may be executed either as a package module (recommended) or directly
as a script. Relative imports require package context, so we provide a safe
fallback to absolute imports and a helpful runtime message about Django setup.
"""

import os
import sys

def import_book_model():
    """Import Book model using package-relative import when possible,
    otherwise try absolute import and finally local import fallback."""
    try:
        # preferred when executed as a module: python -m relationship_app.main
        from .models import Book
        return Book
    except Exception:
        # fall back to absolute import (works when package root is on sys.path)
        try:
            from relationship_app.models import Book
            return Book
        except Exception:
            # last resort: try importing as a plain module if running with cwd==package dir
            try:
                from models import Book
                return Book
            except Exception:
                raise


if __name__ == "__main__":
    try:
        Book = import_book_model()
    except Exception as e:
        print("Import failed. To run this script, run it as a package from the project root:")
        print("  cd <project_root>/django-models/LibraryProject")
        print("  python -m relationship_app.main")
        print("Or start a Django shell with `python manage.py shell` and import models there.")
        print("Detailed error:", repr(e))
        sys.exit(1)

    # At this point Book is imported, but accessing the ORM requires Django settings.
    if "DJANGO_SETTINGS_MODULE" not in os.environ:
        print("DJANGO_SETTINGS_MODULE is not set. To use the Django ORM, either:")
        print("  - Run this from the project root with the project settings available and set DJANGO_SETTINGS_MODULE, e.g:")
        print("      cd <project_root>/django-models/LibraryProject")
        print("      export DJANGO_SETTINGS_MODULE=LibraryProject.settings")
        print("      python -m relationship_app.main")
        print("  - Or use Django's shell which sets up Django for you:")
        print("      cd <project_root>/django-models/LibraryProject")
        print("      python manage.py shell")
        sys.exit(0)

    # If DJANGO_SETTINGS_MODULE is set, try to initialize Django and query the ORM.
    try:
        import django
        django.setup()
        books = Book.objects.all()
        for book in books:
            print(f"{book.title} by {book.author}")
    except Exception as e:
        print("Failed to query Book objects. Make sure Django settings are correct and migrations applied.")
        print("Error:", repr(e))
        sys.exit(1)