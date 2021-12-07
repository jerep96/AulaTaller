import json
import os
import subprocess
import webbrowser
from pathlib import Path
from django.shortcuts import redirect, render, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .models import *

from .forms import *

from .leer_excel import main
from .generate import generate


@login_required
def index(request):
    return render(request, 'index.html')


@login_required
def generar(request):
    form = UploadForm()
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.save()
            data = main(file)
            return render(request, 'generar.html', {'form': form, 'data': data})
    return render(request, 'generar.html', {'form': form})


def pdf(request, data, datos):
    generate(data)
    webbrowser.open_new("./Certificados_Aula_taller.pdf")
    datos = datos.replace("'", '"')
    datos = json.loads(datos)
    context = {'data': datos}
    return render(request, 'generar.html', context)


def subir(request):
    return render(request, 'generar.html')


@login_required
def historial(request):
    archivo = Upload.objects.all()
    BASE_DIR = Path(__file__).resolve().parent.parent
    base = os.path.join(BASE_DIR)
    context = {'archivos': archivo, 'base': base}
    return render(request, 'historial.html', context)


def ver(request):
    #archivo = Upload.objects.all().values()
    datos = DataFile.objects.all().values()
    context = {'data':datos}
    return HttpResponse(context)
