from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import Group
from users.models import CustomUser
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserRegisterForm

    list_display = ('email', 'username', 'is_supporter')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username','first_name','last_name')}),
        ('Profile Info', {'fields': ('image','newsletter')}),
        ('Permissions', {'fields': ('is_active','is_supporter','is_staff','is_superuser')}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.unregister(Group)