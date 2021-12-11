import json
import os
from PyPDF2 import PdfFileMerger
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
            nombreSalida = 'Certificados.pdf'
            fusionador = PdfFileMerger()
            i = 1
            for dato in data:
                name = 'Certificados_Aula_taller' + str(i) + '.pdf'
                generate(dato, name)
                fusionador.append(open('./' + name, 'rb'))
                i += 1
            with open(nombreSalida, 'wb') as salida:
                fusionador.write(salida)
            return render(request, 'generar.html', {'form': form, 'data': data})
    return render(request, 'generar.html', {'form': form})


def pdf(request, data, datos):
    name = 'Certificados_Aula_taller.pdf'
    generate(data, name)
    webbrowser.open_new("./" + name)
    datos = datos.replace("'", '"')
    datos = json.loads(datos)
    context = {'data': datos}
    return render(request, 'generar.html', context)


def allPdf(request, datos):
    webbrowser.open_new("./Certificados.pdf")
    datos = datos.replace("'", '"')
    datos = json.loads(datos)
    context = {'data': datos}
    return render(request, 'generar.html', context)


def subir(request):
    return render(request, 'generar.html')


@login_required
def historial(request):
    user = request.user.username
    if user == 'Carhue':
        archivo = Upload.objects.all()
    '''elif user == 'Trenque':
        sede = 'Trenque Lauquen'
        archivo = Upload.objects.get(sede=sede)
    elif user == 'Olavarria':
        sede = 'Olavarría'
        archivo = Upload.objects.get(sede=sede)
    elif user == 'General':
        sede = 'General Roca'
        archivo = Upload.objects.get(sede=sede)
    elif user == 'GPico':
        sede = 'G. Pico'
        archivo = Upload.objects.get(sede=sede)
    elif user == 'Plata':
        sede = 'Mar del Plata'
        archivo = Upload.objects.get(sede=sede)
    elif user == 'Daireaux':
        sede = 'Daireaux'
        archivo = Upload.objects.get(sede=sede)
    elif user == 'Coronel':
        sede = 'Coronel Suarez'
        archivo = Upload.objects.get(sede=sede)
    elif user == 'Pehuajo':
        sede = 'Pehuajo'
        archivo = Upload.objects.get(sede=sede)
    elif user == 'Lomas':
        sede = 'Tres Lomas'
        archivo = Upload.objects.get(sede=sede)
    elif user == 'Regina':
        sede = 'Villa Regina'   
        archivo = Upload.objects.get(sede=sede)'''

                         
    BASE_DIR = Path(__file__).resolve().parent.parent
    base = os.path.join(BASE_DIR)
    context = {'archivos': archivo, 'base': base, 'traeu': user}
    return render(request, 'historial.html', context)


def ver(request):
    #archivo = Upload.objects.all().values()
    datos = DataFile.objects.all().values()
    context = {'data':datos}
    return HttpResponse(context)
