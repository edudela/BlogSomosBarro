from django.db import models
from django.utils import timezone
from datetime import datetime

# Create your models here.
class Categorias(models.Model):
    nombre = models.CharField(max_length=100)

    def __string__(self):
        print(self.nombre)
        return self.nombre

class Noticias(models.Model):
    autor = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)
    contenido = models.TextField()
    img = models.ImageField(null=True, blank=True, upload_to='img/noticias',help_text="Seleccione una imagen para mostrar")
    creado = models.DateTimeField(default=timezone.now)
    modificado = models.DateTimeField(auto_now=True)
    publicado = models.DateTimeField(blank=True, null=True)
    categorias = models.ManyToManyField('Categorias', related_name='noticias')

    def publicarNoticia(self):
        self.publicado = datetime.now()
        self.save()

    def comentariosAprobados(self):
        return self.comentarios.filter(aprobado=True)

class Comentarios(models.Model):
    noticia = models.ForeignKey('Noticias',related_name='comentarios', on_delete=models.CASCADE)
    autor =  models.ForeignKey('auth.User', on_delete=models.CASCADE)
    cuerpo_comentario = models.TextField()
    creado = models.DateTimeField(default=timezone.now)
    aprobado = models.BooleanField(default=False)

    def aprobarComentario(self):
        self.aprobado = True
        self.save()