from django.urls import path, include
from .views import registrar_cliente, registrar_empleado, user_login, user_logout


app_name = 'cuentas'

urlpatterns = [
    path('registrar/empleado/', registrar_empleado, name='registrar_empleado'),
    path('registrar/cliente/', registrar_cliente, name='registrar_cliente'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
