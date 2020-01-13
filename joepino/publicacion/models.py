from django.db import models

class Publicacion(models.Model):
    titulo = models.CharField(max_length=127)
    descripcion = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

class Capitulo(models.Model):
    titulo = models.CharField(max_length=127)
    orden = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    publicacion = models.ForeignKey('publicacion.Publicacion', related_name='capitulos', on_delete=models.CASCADE)

class Articulo(models.Model):
    titulo = models.CharField(max_length=127)
    orden = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    capitulo = models.ForeignKey('publicacion.Capitulo', related_name='articulos', on_delete=models.CASCADE)

class Parrafo(models.Model):
    texto = models.TextField()
    orden = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    articulo = models.ForeignKey('publicacion.Articulo', related_name='parrafos', on_delete=models.CASCADE)
