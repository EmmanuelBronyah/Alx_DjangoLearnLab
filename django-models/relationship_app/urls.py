from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("list_books/", list_books, name="list-books"),
    path("library_detail/", views.LibraryDetailView.as_view(), name="library-detail"),
    path("register/", views.RegisterView.as_view(), name="register"),
    path('login/', views.RegisterView.as_view(), name="login"),
    path('logout/', views.RegisterView.as_view(), name="logout"),
]
