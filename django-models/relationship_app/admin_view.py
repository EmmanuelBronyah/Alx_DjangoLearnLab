from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def check_role(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'

@user_passes_test(check_role)
def admin_view(request):
    return render(request, 'admin_view.html')
