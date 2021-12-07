from django.db import models
from django.utils import timezone

# Create your models here.

SEDE = (
    ('Carhue', 'Carhue'),
    ('Trenque Lauquen', 'Trenque Lauquen'),
    ('Olavarría', 'Olavarría'),
    ('General Roca', 'General Roca'),
    ('G. Pico', 'G. Pico'),
    ('Mar del Plata', 'Mar del Plata'),
    ('Daireaux', 'Daireaux'),
    ('Coronel Suarez', 'Coronel Suarez'),
    ('Pehuajo', 'Pehuajo'),
    ('Tres Lomas', 'Tres Lomas'),
    ('Villa Regina', 'Villa Regina'),

)

class Upload(models.Model):

    timestamp = models.DateTimeField(default=timezone.now)
    archivo = models.FileField(upload_to='', null=True, blank=True)
    sede = models.CharField(default='Carhue', max_length=50, choices=SEDE, null=True, blank=True)


    class Meta:
        ordering = ['-timestamp']

class DataFile (models.Model):

    dia = models.TextField(null=True, blank=True)
    mes = models.TextField(null=True, blank=True)
    anio = models.TextField(null=True, blank=True)
    nombre = models.TextField(null=True, blank=True)
    apellido = models.TextField(null=True, blank=True)
    dni = models.TextField(null=True, blank=True)
    carrera = models.TextField(null=True, blank=True)
    horas = models.TextField(null=True, blank=True)
    firmaNameI = models.TextField(null=True, blank=True)
    firmaPuestoI = models.TextField(null=True, blank=True)
    firmaNameD = models.TextField(null=True, blank=True)
    firmaPuestoD = models.TextField(null=True, blank=True)
    sede = models.TextField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.nombre}: {self.nombre}'