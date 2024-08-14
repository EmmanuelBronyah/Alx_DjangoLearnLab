from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

class Admin(UserPassesTestMixin, TemplateView):
    template_name = 'admin_view.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.userprofile.role == 'Admin'
