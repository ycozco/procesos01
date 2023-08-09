# En el archivo urls.py de la aplicación "clases"
from django.urls import path
from . import views

app_name = 'clases'

urlpatterns = [
    # Define tus patrones de URL aquí
    path('', views.home_view, name='home'),
    path('lecciones/', views.lista_lecciones, name='lista'),
    path('lecciones/<int:leccion_id>/', views.detalle_leccion, name='detalle_leccion'),
    # Otros patrones de URL
]