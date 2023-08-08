from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


# Create your models here.
class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.TextField()

    class Meta:
        db_table = 'Categorias'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Categorias'  # Nombre en plural

class Lecciones(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.TextField()
    descripcion = models.TextField()
    contenido_texto = models.TextField()
    ruta_imagen = models.TextField()
    ruta_recurso = models.TextField()
    id_categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE)
    status = models.TextField()

    class Meta:
        db_table = 'Lecciones'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Lecciones'  # Nombre en plural

class Ejercicios(models.Model):
    id = models.AutoField(primary_key=True)
    id_leccion = models.ForeignKey(Lecciones, on_delete=models.CASCADE)
    enunciado = models.TextField()
    ruta_imagen = models.TextField()

    class Meta:
        db_table = 'Ejercicios'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Ejercicios'  # Nombre en plural

class Respuestas(models.Model):
    id = models.AutoField(primary_key=True)
    id_ejercicio = models.ForeignKey(Ejercicios, on_delete=models.CASCADE)
    texto_respuesta = models.TextField()
    es_correcta = models.BooleanField()

    class Meta:
        db_table = 'Respuestas'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Respuestas'  # Nombre en plural


# Resto de los modelos, sigue el mismo patrón para especificar los nombres de las tablas
class Evaluaciones(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_leccion = models.ForeignKey(Lecciones, on_delete=models.CASCADE)
    fecha = models.DateTimeField()
    calificacion = models.IntegerField()

    class Meta:
        db_table = 'Evaluaciones'  # Nombre de la tabla en la base de datos
        verbose_name_plural = 'Evaluaciones'  # Nombre en plural

class Resultados(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_respuesta = models.ForeignKey(Respuestas, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Resultados'
        verbose_name_plural = 'Resultados' # nombre en plural

class Progresos(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_leccion = models.ForeignKey(Lecciones, on_delete=models.CASCADE)
    completada = models.BooleanField()

    class Meta:
        db_table = 'Progresos'
        verbose_name_plural = 'Progresos' # nombre en plural

class Puntuaciones(models.Model):
    id = models.AutoField(primary_key=True)
    id_usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    id_leccion = models.ForeignKey(Lecciones, on_delete=models.CASCADE)
    puntuacion = models.IntegerField()

    class Meta:
        db_table = 'Puntuaciones'
        verbose_name_plural = 'Puntuaciones' # nombre en plural
