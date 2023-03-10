from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserAdminChangeForm,UserAdminCreationForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['reg', 'admin']
    list_filter = ['admin','staff','active']
    fieldsets = (
        (None, {'fields': ('reg', 'password')}),
        ('Personal info', {'fields': ('full_name',)}),
        ('Permissions', {'fields': ('admin','staff','active',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('reg', 'password', 'password_2')}
        ),
    )
    search_fields = ['reg',]
    ordering = ['reg']
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)
