from .forms import SignUpForm, UserRegisterForm
from django.shortcuts import redirect, render
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib import messages
from django_email_verification import send_email
from django.contrib.auth.models import User

class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'account/register.html'
  success_url = reverse_lazy('login')
  form_class = SignUpForm
  success_message = "Your profile was created successfully"

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            user = User.objects.get(username=username,email=email)
            user.is_active = False
            send_email(user)
            messages.success(
                request, f'Your account has been created! Please go into your mail and confirm your account to login')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})