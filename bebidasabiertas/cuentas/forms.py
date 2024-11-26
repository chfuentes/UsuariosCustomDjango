from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class EmployeeCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name',
                  'last_name', 'phone')

    # No tiene sentido el clean; Para que voy a marcar o asegurarme que no se marque
    # un cliente como empleado? si puedo hacer que se marque automatico y no lo muestro?
    # Como lo hago? Cuando creo un cliente le muestro el formulario de cliente
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_employee = True
        user.is_client = False
        if commit:
            user.save()
        return user


class ClientCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'phone', 'birth_date', 'address')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_client = True
        user.is_employee = False
        if commit:
            user.save()
        return user


class EmployeeChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name',
                  'last_name', 'phone')


class ClientChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name',
                  'phone', 'birth_date', 'address')
