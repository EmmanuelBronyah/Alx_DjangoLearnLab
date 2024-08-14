def check_role_member(user):
    return user.is_authenticated and user.userprofile.role == 'Member'
