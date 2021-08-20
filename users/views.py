from .forms import UserRegisterForm, UserUpdateForm
from django.shortcuts import redirect, render
from django.contrib import messages
from django_email_verification import send_email
from .decorators import unauthenticated_user
from django.contrib.auth.decorators import login_required
from .models import CustomUser
from friendship.models import Friend,Follow,Block
from django.urls import reverse

@unauthenticated_user
def register(request):
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
                Please go into your mails and confirm your account to login''')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,request.FILES,instance=request.user)
        if u_form.is_valid():
            u_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
    return render(request, 'account/profile.html', {'u_form': u_form})


@login_required
def users_profile(request, pk):
    other_user = CustomUser.objects.get(pk=pk)
    followers = Follow.objects.followers(other_user)
    friends = Friend.objects.friends(other_user)
    blocked = Block.objects.blocked(other_user)
    friendsCount = len(Friend.objects.friends(other_user))
    followersCount = len(Follow.objects.followers(other_user))
    unreadfriendrequestsCount = Friend.objects.unread_request_count(user=other_user)
    unreadfriendrequests = Friend.objects.unread_requests(user=other_user)
    sentfriendrequest = Friend.objects.sent_requests(user=request.user)

    context = {
        "other_user": other_user,
        "followers": followers,
        "friends": friends,
        "blocked": blocked,
        "friendsCount":friendsCount,
        "followersCount":followersCount,
        "unreadfriendrequestsCount":unreadfriendrequestsCount,
        "unreadfriendrequests":unreadfriendrequests,
        "sentfriendrequest" : sentfriendrequest
    }

    return render(request, "account/user-profile.html", context)