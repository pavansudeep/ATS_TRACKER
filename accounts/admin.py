from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'first_name', 'last_name', 'is_staff', 'is_student', 'is_admin_user']
    fieldsets = UserAdmin.fieldsets + (
        ('Custom Roles', {'fields': ('is_student', 'is_admin_user')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Custom Roles', {'fields': ('is_student', 'is_admin_user')}),
    )

admin.site.register(CustomUser, CustomUserAdmin)
