from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError


class CustomUser(AbstractUser):
    # Campos comunes
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=9, blank=True)

    # Campos específicos para cada tipo de usuario
    birth_date = models.DateField(null=True, blank=True)  # Solo para Clientes
    address = models.CharField(
        max_length=255, blank=True)  # Solo para Clientes

    # Tipo de usuario
    is_employee = models.BooleanField(default=False)  # Empleado
    is_client = models.BooleanField(default=False)  # Cliente

    # Relaciones con grupos y permisos
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_groups_set',
        blank=True,
        help_text='Los grupos a los que este usuario pertenece.',
        verbose_name='grupos',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permission_set',
        blank=True,
        help_text='Permisos específicos para este usuario.',
        verbose_name='permisos del usuario',
    )

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email  # Si no se asignó username, usar el email
        if self.is_employee and self.is_client:
            raise ValidationError(
                "Un usuario no puede ser tanto empleado como cliente.")
        if self.is_employee:
            self.birth_date = None
            self.address = ''
        super().save(*args, **kwargs)
