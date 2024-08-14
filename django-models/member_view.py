from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

def check_role(user):
    return user.is_authenticated and user.userprofile.role == 'Member'

@user_passes_test(check_role)
def member_view(request):
    return render(request, 'member_view.html')
