from django.contrib import admin

from certificado.models import DataFile, Upload

# Register your models here.
admin.site.register(DataFile)
admin.site.register(Upload)