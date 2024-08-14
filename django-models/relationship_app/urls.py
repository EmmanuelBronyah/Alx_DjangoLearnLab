from django.urls import path
from .views import list_books
from .views import LibraryDetailView
from .views import RegisterView
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path("list_books/", list_books, name="list-books"),
    path("library_detail/", views.LibraryDetailView.as_view(), name="library-detail"),
    path("register/", views.register, name="register"),
    path('login/', views.LoginView.as_view(template_name="relationship_app/login.html"), name="login"),
    path('logout/', views.LogoutView.as_view(template_name="relationship_app/logout.html"), name="logout"),
]
