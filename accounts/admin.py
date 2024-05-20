from django.contrib import admin
from .models import Account
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class AccountAdmin(UserAdmin):
    list_display = ('email','username', 'first_name', 'last_name', 'phone_number', 'date_joined', 'last_login', 'is_admin', 'is_staff', 'is_superuser')
    search_fields = ('email', 'username', 'first_name', 'last_name', 'phone_number')
    readonly_fields = ('date_joined', 'last_login')
    ordering = ('email',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Account, AccountAdmin)
#
# The code above is the admin.py file for the accounts app. It registers the Account model with the Django admin site.
#
# The AccountAdmin class is a subclass of UserAdmin. It customizes the display of the Account model in the Django admin site.
#
# The list_display attribute specifies the fields to display in the list view of the Account model.
# The search_fields attribute specifies the fields to search for in the list view.
# The readonly_fields attribute specifies the fields that are read-only in the admin interface.
# The filter_horizontal attribute specifies the fields that are displayed as horizontal filter widgets.
# The list_filter attribute specifies the fields to filter the list view by.
# The fieldsets attribute specifies the fieldsets for the add and change forms.
# The add_fieldsets attribute specifies the fieldsets for the add form.
# The ordering attribute specifies the default ordering of the list view.
# The filter_horizontal attribute specifies the fields that are displayed as horizontal filter widgets.
# Finally, the admin.site.register(Account, AccountAdmin) line registers the Account model with the custom AccountAdmin class.
#
# This code customizes the display of the Account model in the Django admin site, making it easier to manage user accounts.
#
# Note: The UserAdmin class is a built-in Django admin class that provides a default admin interface for user models. By subclassing UserAdmin, you can customize the display of user models in the admin site.
#
# If you don't need to customize the display of the Account model in the admin site, you can register the model without the custom AccountAdmin class like this:
#
#
# from django.contrib import admin
# from .models import Account
#