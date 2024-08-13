from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic import TemplateView

class AdminView(UserPassesTestMixin, TemplateView):
    template_name = 'admin_view.html'

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user.userprofile.role == 'Admin'

    def handle_no_permission(self):
        # Optional: Redirect to a custom page or show a message if the user does not have permission
        return redirect('login')
