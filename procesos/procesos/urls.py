
from django.contrib import admin
from django.urls import path, include,path
from django.conf import settings
from django.conf.urls.static import static
from clases import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('clases.urls')),  # Incluye las URLs de la app 'clases'
    # Otras URLs de tu proyecto pueden ir aquí

]

# Agrega la siguiente línea para servir los archivos estáticos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
