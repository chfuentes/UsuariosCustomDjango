from django.shortcuts import render


def home(request):
    user = request.user
    if user.is_authenticated:
        context = {
            'is_employee': user.is_employee,
            'is_client': user.is_client,
            'is_superuser': user.is_superuser,
        }
    else:
        context = {'no_logueado': user}
    return render(request, 'home.html', context)
