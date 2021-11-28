
from django.shortcuts import redirect, render,HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from .forms import *

from leer_excel import *

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
            #leer_excel.main()
            print(form)
    return render(request, 'generar.html', {'form':form})

def subir(request):

    return render(request, 'generar.html')

@login_required
def historial(request):
    archivo = Upload.objects.all()
    context = {'archivos': archivo}
    return render(request, 'historial.html', context)

def ver (request):
    archivo = Upload.objects.all().values()
    return HttpResponse(archivo)