from django.contrib import admin
from .models import Evaluaciones, Resultados, Progresos, Puntuaciones, Lecciones, Ejercicios ,Respuestas, Categorias
@admin.register(Evaluaciones)
class EvaluacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_usuario', 'id_leccion', 'fecha', 'calificacion')

@admin.register(Resultados)
class ResultadosAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_usuario', 'id_respuesta')

@admin.register(Progresos)
class ProgresosAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_usuario', 'id_leccion', 'completada')

@admin.register(Puntuaciones)
class PuntuacionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_usuario', 'id_leccion', 'puntuacion')

@admin.register(Lecciones)
class LeccionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'titulo', 'descripcion', 'contenido_texto', 'ruta_imagen', 'ruta_recurso', 'id_categoria', 'status')

@admin.register(Categorias)
class CategoriasAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')

@admin.register(Ejercicios)
class EjerciciosAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_leccion', 'enunciado', 'ruta_imagen')

@admin.register(Respuestas)
class RespuestasAdmin(admin.ModelAdmin):
    list_display = ('id', 'id_ejercicio', 'texto_respuesta', 'es_correcta')

