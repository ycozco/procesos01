from django.shortcuts import render, get_object_or_404
from .models import Lecciones

def home_view(request):
    return render(request, 'home.html')

def lista_lecciones(request):
    lecciones = Lecciones.objects.all()  # Obtén todas las lecciones
    context = {
        'lecciones': lecciones
    }
    return render(request, 'lista_lecciones.html', context)


def detalle_leccion(request, leccion_id):
    leccion = get_object_or_404(Lecciones, id=leccion_id)
    context = {
        'leccion': leccion
    }
    return render(request, 'detalle_leccion.html', context)