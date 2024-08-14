from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def check_role(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

@user_passes_test(check_role)
def librarian_view(request):
    return render(request, 'librarian_view.html')
