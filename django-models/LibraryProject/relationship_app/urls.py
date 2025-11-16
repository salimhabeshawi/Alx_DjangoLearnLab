from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),

    path('login/',
         LoginView.as_view(template_name='relationship_app/login.html'),
         name='login'),

    path('logout/',
         LogoutView.as_view(template_name='relationship/logout.html'),
         name='logout'),

    # your existing library path
    path('library/<int:pk>/', views.library_detail_view, name='library-detail'),
]
