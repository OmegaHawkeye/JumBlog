from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import UpdateView
from .forms import UserRegisterForm, UserUpdateForm
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages
from django_email_verification import send_email
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from .models import CustomUser

# @unauthenticated_user
def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = CustomUser.objects.get(username=username, email=email)
            user.is_active = False
            send_email(user)
            messages.success(
                request, f'''Your account has been created! 
                Please go into your mail and confirm your account to login''')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        # p_form = ProfileUpdateForm(request.POST,
        #                                request.FILES,
        #                                instance=request.user.profile)
        u_form = UserUpdateForm(request.POST,request.FILES,instance=request.user)
        if u_form.is_valid(): #and p_form.is_valid():
            u_form.save()
            # p_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        # p_form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'account/profile.html', {'u_form': u_form})


class CustomUserUpdateView(UpdateView,LoginRequiredMixin,UserPassesTestMixin):
    template_name = "account/user-profile.html"
    model = CustomUser
    form_class = UserUpdateForm
    success_url = "/home/"

    def get_success_url(self):
        return reverse("user-profile",kwargs={"pk": self.object.id}) 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        profile = self.get_object()
        if self.request.user == profile.user:
            return True
        return False