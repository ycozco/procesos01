
from django.contrib import admin
from django.urls import path, include,path
from django.conf import settings
from django.conf.urls.static import static
from clases import views
urlpatterns = [
    path('', views.inicio_view, name='inicio'),
    path('admin/', admin.site.urls),
    path('clases/', include('clases.urls')),  # o el nombre de la app donde tengas tus urls
]

# Agrega la siguiente línea para servir los archivos estáticos
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
