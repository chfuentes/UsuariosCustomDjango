from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import EmployeeCreationForm, ClientCreationForm
from django.contrib.auth.decorators import login_required


def user_login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            if 'next' in request.POST:
                return redirect(request.POST.get("next"))
            else:
                return redirect("home")
    else:
        form = AuthenticationForm()
    return render(request, "cuentas/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect('home')


@login_required
def registrar_empleado(request):
    if request.method == 'POST':
        form = EmployeeCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EmployeeCreationForm()
    return render(request, 'cuentas/registrar_empleado.html', {'form': form})


@login_required
def registrar_cliente(request):
    if request.method == 'POST':
        form = ClientCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ClientCreationForm()
    return render(request, 'cuentas/registrar_cliente.html', {'form': form})
