from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

class Librarian(UserPassesTestMixin, TemplateView):
    template_name = 'librarian_view.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.userprofile.role == 'Librarian'
