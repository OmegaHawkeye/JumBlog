from django.contrib.auth.mixins import UserPassesTestMixin

class SupportRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user.is_supporter