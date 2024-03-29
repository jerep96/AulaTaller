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
    with open("./" + name, 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/pdf")
        response['Content-Disposition'] = 'inline; filename=' + name
        return response


def allPdf(request, datos):
    with open("./Certificados.pdf", 'rb') as fh:
        response = HttpResponse(fh.read(), content_type="application/pdf")
        response['Content-Disposition'] = 'inline; filename=Certificados.pdf'
        return response


def subir(request):
    return render(request, 'generar.html')


@login_required
def historial(request):
    user = request.user.username
    form= HistoryForm()
    archivo = Upload.objects.all()
    if user == 'Carhue':
        archivo = Upload.objects.all()
    elif user == 'Trenque':
        sede = 'Trenque Lauquen'
        archivo = Upload.objects.filter(sede=sede).values()
    elif user == 'Olavarria':
        sede = 'Olavarría'
        archivo = Upload.objects.filter(sede=sede).values()
    elif user == 'General':
        sede = 'General Roca'
        archivo = Upload.objects.filter(sede=sede).values()
    elif user == 'GPico':
        sede = 'G. Pico'
        archivo = Upload.objects.filter(sede=sede).values()
    elif user == 'Plata':
        sede = 'Mar del Plata'
        archivo = Upload.objects.filter(sede=sede).values()
    elif user == 'Daireaux':
        sede = 'Daireaux'
        archivo = Upload.objects.filter(sede=sede).values()
    elif user == 'Coronel':
        sede = 'Coronel Suarez'
        archivo = Upload.objects.filter(sede=sede).values()
    elif user == 'Pehuajo':
        sede = 'Pehuajo'
        archivo = Upload.objects.filter(sede=sede).values()
    elif user == 'Lomas':
        sede = 'Tres Lomas'
        archivo = Upload.objects.filter(sede=sede).values()
    elif user == 'Regina':
        sede = 'Villa Regina'   
        archivo = Upload.objects.filter(sede=sede).values()
    if request.method == 'POST':
        form = HistoryForm(request.POST)
        if form.is_valid():
            res = request.POST
            if res['sede'] == 'Carhue':
                archivo = Upload.objects.all()
            else:
                archivo = Upload.objects.filter(sede=res['sede']).values()
    # archivo = Upload.objects.all()
    BASE_DIR = Path(__file__).resolve().parent.parent
    base = os.path.join(BASE_DIR)
    context = {'archivos': archivo, 'base': base, 'traeu': user, 'form': form}
    return render(request, 'historial.html', context)


def ver(request):
    #archivo = Upload.objects.all().values()
    datos = DataFile.objects.all().values()
    context = {'data':datos}
    return HttpResponse(context)
