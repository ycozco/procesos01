# En el archivo urls.py de la aplicación "clases"
from django.urls import path
from . import views

app_name = 'clases'

urlpatterns = [
    path('', views.home_view, name='home'),
    path('perfil/', views.profile_view, name='perfil'),
    path('registro/', views.registro_view, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('lecciones/', views.lista_lecciones, name='lista'),
    path('lecciones/<int:leccion_id>/', views.detalle_leccion, name='detalle_leccion'),
]
