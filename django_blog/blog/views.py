from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


def register_view(request):
    error = None
    form = CreateUserForm()
    if request.method == "POST":
      form = CreateUserForm(request.POST)
      if form.is_valid():
        try:
          form.save()
          return redirect("profile")
        except ValidationError as e:
          error = "An error occurred while processing your registration."
      else:
        error = "There are errors in the form. Please correct them."
      
    context = {"form": form, "error": error}
    return render(request, "blog/register.html", context)


def login_view(request):
    error = None
    if request.method == "POST":
      username = request.POST.get("username")
      password = request.POST.get("password")
      
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        return redirect('profile')
      else:
        error = "User not found."
    context = {"error": error}

    return render(request, "blog/login.html", context)

login_required(login_url="register")
def profile_view(request):
    context = {}

    return render(request, "blog/profile.html", context)

login_required(login_url="register")
def edit_profile_view(request):
  user = request.user
  if request.method == "POST":
    new_username = request.POST.get("new_username")
    new_email = request.POST.get("new_email")
    
    if new_username is not None:
      user.username = new_username
    if new_email is not None:
      user.email = new_email
    user.save()
    
    return redirect("profile")
  
  context = {}
  return render(request, "blog/edit_profile.html", context)


def logout_view(request):
    logout(request)
    return redirect("login")
  
    context = {}
    return render(request, "blog/logout.html", context)
