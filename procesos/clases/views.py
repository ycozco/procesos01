from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Evaluaciones, Resultados, Progresos, Puntuaciones


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('perfil')  # Redirige a la página después del inicio de sesión exitoso
        else:
            # Si las credenciales son incorrectas, muestra un mensaje de error en el template
            error_message = "Credenciales inválidas. Inténtalo de nuevo."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
def logout_view(request):
    logout(request)
    return redirect('login')  # Redirige a la vista de login después de hacer logout

@login_required
def profile_view(request):
    user = request.user

    # Obtener las evaluaciones del usuario
    evaluaciones = Evaluaciones.objects.filter(id_usuario=user)

    # Obtener los resultados del usuario
    resultados = Resultados.objects.filter(id_usuario=user)

    # Obtener el progreso del usuario
    progreso = Progresos.objects.filter(id_usuario=user)

    # Obtener las puntuaciones del usuario
    puntuaciones = Puntuaciones.objects.filter(id_usuario=user)

    return render(request, 'perfil.html', {'user': user, 'evaluaciones': evaluaciones, 'resultados': resultados, 'progreso': progreso, 'puntuaciones': puntuaciones})

def inicio_view(request):
    return render(request, 'inicio.html')