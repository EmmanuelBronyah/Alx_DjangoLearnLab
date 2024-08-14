from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

class Member(UserPassesTestMixin, TemplateView):
    template_name = 'member_view.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.userprofile.role == 'Member'
