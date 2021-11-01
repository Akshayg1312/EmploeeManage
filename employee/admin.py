from django.contrib import admin

from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser,EmployeeModel



class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'address', 'dob','company')     # display list in Admin Panel
    list_filter = ('email', 'is_staff', 'is_active',)     # Set Filter in admin panel
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'is_staff','first_name','last_name', 'is_active','address','dob','company')}    #Added Extra fields define here
        ),
    )
    search_fields = ('email',)  # Searching base on email
    ordering = ('email',)       # Ordering base on email


admin.site.register(CustomUser, CustomUserAdmin)     #Register CustomUser on admin panel

   

admin.site.register(EmployeeModel)                   #Register EmployeeModel on admin panel
