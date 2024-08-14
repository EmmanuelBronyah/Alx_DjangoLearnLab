def check_role_admin(user):
    return user.is_authenticated and user.userprofile.role == 'Admin'
