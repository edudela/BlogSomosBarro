from django.contrib import admin
from .models import Categorias, Noticias, Comentarios

# Register your models here.
admin.site.register(Categorias,admin.ModelAdmin)
admin.site.register(Noticias,admin.ModelAdmin)
admin.site.register(Comentarios,admin.ModelAdmin)

