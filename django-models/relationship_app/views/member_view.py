from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

class RoleRequiredMixin(UserPassesTestMixin):
    role = None

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.userprofile.role == self.role

class LibrarianView(RoleRequiredMixin, TemplateView):
    template_name = 'member_view.html'
    role = 'Member'