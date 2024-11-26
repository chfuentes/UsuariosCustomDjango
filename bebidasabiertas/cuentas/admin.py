from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import EmployeeCreationForm, EmployeeChangeForm, ClientCreationForm, ClientChangeForm


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['email', 'username', 'first_name', 'last_name',
                    'is_staff', 'is_active', 'is_employee', 'is_client']
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('phone', 'birth_date',
         'address', 'is_employee', 'is_client')}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('phone', 'birth_date',
         'address', 'is_employee', 'is_client')}),
    )

    def get_form(self, request, obj=None, **kwargs):
        if obj is None:  # Adding a new user
            if request.path.endswith('add/'):
                if 'is_employee' in request.GET:
                    self.add_form = EmployeeCreationForm
                elif 'is_client' in request.GET:
                    self.add_form = ClientCreationForm
        else:  # Changing an existing user
            if obj.is_employee:
                self.form = EmployeeChangeForm
            elif obj.is_client:
                self.form = ClientChangeForm
        return super().get_form(request, obj, **kwargs)


admin.site.register(CustomUser, CustomUserAdmin)
