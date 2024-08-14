# 'Admin' view
def check_role(user, role):
  return user.is_authenticated and user.userprofile.role == role

@user_passes_test(lambda user: check_role(user, 'Admin'))
def admin_view(request):
    return render(request, 'admin_view.html')