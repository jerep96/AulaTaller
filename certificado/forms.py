from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Upload


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

class UploadForm(forms.ModelForm):
    archivo = forms.FileField(label='Importar', required=False)
    sede = forms.ChoiceField(label='Seleccione una sede', widget=forms.Select(attrs={'rows': 2, 'class': 'form-select'}),
                             choices=SEDE)

    class Meta:
        model = Upload
        fields = ['archivo', 'sede']