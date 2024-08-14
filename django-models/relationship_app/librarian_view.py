def check_role_librarian(user):
    return user.is_authenticated and user.userprofile.role == 'Librarian'

