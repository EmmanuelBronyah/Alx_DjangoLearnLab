from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

class AdminView(UserPassesTestMixin, TemplateView):
    template_name = 'relationship_app/admin_view.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.userprofile.role == 'Admin'
