from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import register
from .views import LoginView
from .views import LogoutView
from . import views

urlpatterns = [
    path("list_books/", list_books, name="list-books"),
    path("library_detail/", views.LibraryDetailView.as_view(), name="library-detail"),
    path("register/", views.register, name="register"),
    path("login/", views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path("logout/", views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
    path("books/add/", views.add_book, name="add-book"),
    path("books/<int:book_id>/edit/", views.edit_book, name="edit-book"),
    path("books/<int:book_id>/delete/", views.delete_book, name="delete-book")
]
