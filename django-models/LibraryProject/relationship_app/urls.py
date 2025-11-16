from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship/logout.html'), name='logout'),
    # your existing library path
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
    path('role/admin/', views.admin_view, name='admin_view'),
    path('role/librarian/', views.librarian_view, name='librarian_view'),
    path('role/member/', views.member_view, name='member_view'),
    path("book/add/", views.add_book, name="add_book/"),
    path("book/<int:pk>/edit/", views.edit_book, name="edit_book/"),
    path("book/<int:pk>/delete/", views.delete_book, name="delete_book/"),
]