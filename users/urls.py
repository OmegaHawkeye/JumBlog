from django.urls import path
from .views import *
from django.contrib.auth.views import *


urlpatterns = [
    #path("profile/<int:pk>/",CustomUserUpdateView.as_view(),name="user-profile"),
    path("profile/",profile,name="profile"),
    path("register/",Register,name="register"),
    path('login/', LoginView.as_view(template_name='account/login.html',
                                     redirect_authenticated_user=True), name='login'),
    path('logout/', LogoutView.as_view(template_name='account/logout.html'), name='logout'),
    path("password-change/", PasswordChangeView.as_view(
        template_name="account/password-change.html"), name="password_change"),
    path("password-change/done", PasswordChangeDoneView.as_view(
        template_name="account/password-change-done.html"), name="password_change_done"),
    path('password-reset/',
         PasswordResetView.as_view(
             template_name='account/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(
             template_name='account/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
             template_name='account/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(
             template_name='account/password_reset_complete.html'
         ),
         name='password_reset_complete'),
]
