import os
from pathlib import Path
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *

from .leer_excel import main

@login_required
def index(request):
    return render(request, 'index.html')

@login_required
def generar(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            main(request.FILES)
            print(form)
    return render(request, 'generar.html', {'form':form})

def subir(request):

    return render(request, 'generar.html')

@login_required
def historial(request):
    archivo = Upload.objects.all()
    BASE_DIR = Path(__file__).resolve().parent.parent
    base = os.path.join(BASE_DIR)
    context = {'archivos': archivo, 'base': base}
    return render(request, 'historial.html', context)

def ver (request):
    archivo = Upload.objects.all().values()
    return HttpResponse(archivo)