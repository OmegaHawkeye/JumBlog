from .forms import UserRegisterForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django_email_verification import send_email
from django.contrib.auth.models import User
from .decorators import unauthenticated_user

@unauthenticated_user
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