from users.models import CustomUser,Feature,Role
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegisterForm

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    add_form = UserRegisterForm

    list_display = ('email', 'username', 'role')
    fieldsets = (
        (None, {'fields': ('email','username','role')}),
        ('Personal info', {'fields': ('first_name','last_name')}),
        ('Profile Info', {'fields': ('image','newsletter','xp','features')}),
        ('Permissions', {'fields': ('groups','is_active','is_supporter','is_staff','is_superuser')}),
    )

admin.site.register(CustomUser,CustomUserAdmin)
admin.site.register(Role)
admin.site.register(Feature)