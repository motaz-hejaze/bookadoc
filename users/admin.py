from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import get_user_model
# Register your models here.

UserModel = get_user_model()

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = UserModel
    list_display = ('email', 'is_staff', 'is_active', 'user_type')
    list_filter = ('email', 'is_staff', 'is_active', 'user_type')
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name','last_name','email','user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser','groups','user_permissions')}),
        ('Important dates', {'fields': ('last_login','date_joined')}),
    )
    add_fieldsets = (
        ('Personal info', {'fields': ('username', 'password1', 'password2','email','user_type')}),
        ('Permissions', {'fields': ('is_staff', 'is_active','is_superuser')}),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(UserModel, CustomUserAdmin)