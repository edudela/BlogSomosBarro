from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
def index(request):
    return render(request,'index.html',{})

'''def quienessomos(request):
    return render(request, 'quienessomos.html')
'''