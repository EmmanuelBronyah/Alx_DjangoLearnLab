from django.shortcuts import render
from .models import Book, Library
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.views import LoginView, LogoutView


def list_books(request):
  books = Book.objects.all()
  context = {"books": books}
  return render(request, "relationship_app/list_books.html", context)


class LibraryDetailView(ListView):
  model = Library
  context_object_name = "library"
  template_name = "relationship_app/library_detail.html"
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["library"] = Library.objects.all()
        return context

def register(request):
  if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
  else:
      form = UserCreationForm()
  return render(request, 'relationship_app/register.html', {'form': form})

class LoginView(LoginView):
    template_name = 'login.html'

class LogoutView(LogoutView):
    template_name = 'logout.html'
