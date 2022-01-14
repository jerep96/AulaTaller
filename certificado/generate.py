# -*- coding: utf-8 -*-
import json
import os

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.styles import ParagraphStyle

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


def generate(data, name):
    try:
        data = data.replace("'", '"')
        data = json.loads(data)
    except:
        pass
    '''pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
    pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))'''
    pdfmetrics.registerFont(TTFont('DejaVuSans','DejaVuSans.ttf'))
    pdfmetrics.registerFont(TTFont('DejaVuSansBd','DejaVuSans-Bold.ttf'))
    style = ParagraphStyle(
        name='Normal',
        fontName='DejaVuSans',
        fontSize=8,
    )
    Paragraph('text', style, bulletText=None)
    w, h = A4
    x = h - 640
    y = 40
    c = canvas.Canvas(name, pagesize=A4)
    c.setPageSize(landscape(A4))
    c.drawImage('certificado/static/img/uflo.jpg', 20, 40, width=155, height=530)
    c.drawImage('certificado/static/img/title_cuadro.png', 190, 40, width=620, height=530)
    # c.setFont('roboto', 16)
    c.setFont('DejaVuSans', 18)
    c.drawString(270, 450, "Por cuanto ___________________________________________,")
    c.setFont('DejaVuSansBd', 18)
    c.drawString(390, 450, str(data['Apellido']) + ', ' + str(data['Nombre']))
    c.setFont('DejaVuSans', 16)
    c.drawString(300, 410, "DNI. _______________, ha dado cumplimiento con los")
    c.drawString(350, 410, str(data['DNI'])[0:2]+'.'+str(data['DNI'])[2:5]+'.'+str(data['DNI'])[5:8])
    c.drawString(340, 370, "requisitos de aprobación del curso de")
    c.drawString(240, 320, "________________________________________________________________")
    c.setFont('DejaVuSansBd', 20)
    c.drawString(370, 320, str(data['Curso']))
    c.setFont('DejaVuSans', 16)
    c.drawString(250, 280, "dictado por Aula Taller Capacitaciones con el aval académico de")
    c.drawString(250, 250, "la Universidad de Flores con una carga horaria de ___ horas reloj.")
    c.drawString(650, 250, str(data['Horas']))
    c.setFont('DejaVuSans', 12)
    c.drawString(340, 210, "Se extiende el presente Certificado que así lo acredita,")
    c.drawString(320, 190, "en la Ciudad Autónoma de Buenos Aires, República Argentina,")
    c.drawString(355, 170, "a los __ días del mes de ____________ del año ____.")
    c.drawString(385, 170, str(data['Dia']))
    c.drawString(505, 170, str(data['Mes']))
    c.drawString(625, 170, str(data['Anio']))

    # Firmas - Lineas
    c.line(x + 30, 100, x + 200, 100)
    c.line(x + 210, 100, x + 380, 100)
    c.line(x + 390, 100, x + 560, 100)

    # Firmas - texto Medio
    c.setFont('DejaVuSans', 8)
    c.drawString(470, 80, "Lic. Natalia Arias")
    c.drawString(430, 70, "Secretaria Regional de Vinculación.")
    c.drawString(490, 60, "UFLO")

    # Firmas - texto Izquierda
    c.setFont('DejaVuSans', 8)
    c.drawString(270, 80, str(data['Nombre Iz']))
    c.drawString(297, 70, str(data['Puesto Iz']))
    c.drawString(265, 60, str(data['Abajo Iz']))

    # Firmas - texto Derecha
    c.setFont('DejaVuSans', 8)
    c.drawString(640, 80, str(data['Nombre D']))
    c.drawString(655    , 70, str(data['Puesto D']))
    c.drawString(630, 60, str(data['Abajo D']))

    c.save()

    return c
