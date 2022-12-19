from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Noticias, Comentarios, Categorias
from django.http.response import Http404
from .forms import CommentarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def index(request):
    #texto = {'mensaje_texto': 'Esta es mi primer pagina :)'}
    ultimasnoticias = Noticias.objects.all().order_by('creado').reverse()[:3]
    context ={
        'noticiasdestacadas':ultimasnoticias,
        "MEDIA_ROOT": 'media/img/noticias/'
    }
    return render(request, 'index.html',context)
'''
def index(request):
    return render(request,'index.html',{})
'''
def quienessomos(request):
    return render(request, 'quienessomos.html',{})

def noticiasdetalle(request,id):
    try:
        datanoticia = Noticias.objects.get(id=id)
        lista_comentarios = Comentarios.objects.filter(aprobado=True)
    except Noticias.DoesNotExist:
        raise Http404('La Noticia solicitada no existe')

    form=CommentarioForm()
    if request.method=='POST':
        form = CommentarioForm(request.POST)
        if form.is_valid():
            print("Validacion exitosa!")
            print("Autor:" + form.cleaned_data["autor"])
            print("Comentario:" + form.cleaned_data["cuerpo_comentario"])
            comment = Comentarios(
                autor=form.cleaned_data["autor"],
                cuerpo_comentario=form.cleaned_data["cuerpo_comentario"],
                noticia=datanoticia
            )
            comment.save()

    context = {
        "noticia": datanoticia,
        "comentarios":lista_comentarios,
        "MEDIA_ROOT": 'media/img/noticias/',
        'comentario_form':form
        
    }

    return render(request,'detalle-noticia.html',context)

@login_required
def comment_approve(request, id):
    try:
        comentarios =Comentarios.objects.get(id =id)
    except Comentarios.DoesNotExist:
        raise Http404('Comentario no existe')
    comentarios.approve()
    return redirect('detalle-noticia', id=comentarios.noticia.id)


@login_required
def comment_remove(request, id):
    try:
        comentario =Comentarios.objects.get(id =id)
    except Comentarios.DoesNotExist:
        raise Http404('Comentario no existe')
    noticia_id = comentario.noticia.id
    comentario.delete()
    return redirect('detalle-noticia', id=noticia_id)
