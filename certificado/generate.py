from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, landscape
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor

from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
def generate(nombre, Sede, dni, carrera,carga_horaria,dia,mes,anio):
    pdfmetrics.registerFont(TTFont('Vera', 'Vera.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBd', 'VeraBd.ttf'))
    pdfmetrics.registerFont(TTFont('VeraIt', 'VeraIt.ttf'))
    pdfmetrics.registerFont(TTFont('VeraBI', 'VeraBI.ttf'))

    '''nombre = "Palacios Toconas Omar Jeremias"
    Sede = "UFLO"
    dni = "39.443.824"
    carrera = "Tecnicatura Superior en Desarrollo de Software"
    carga_horaria = "350"
    dia = "25"
    mes = "Noviembre"
    anio = "2021"'''
    w, h = A4
    x = h - 640
    y = 40
    c = canvas.Canvas("Certificados_Aula_taller.pdf", pagesize=A4)
    c.setPageSize(landscape(A4))
    c.drawImage('certificado/static/img/uflo.jpg', 20,40, width=155, height=530)
    c.drawImage('certificado/static/img/title_cuadro.png', 190,40, width=620, height=530)
    #c.setFont('roboto', 16)
    c.setFont('Vera', 18)
    c.drawString(270, 450, "Por cuanto ___________________________________________,")
    c.drawString(390, 450, nombre)
    c.setFont('Vera', 16)
    c.drawString(300, 410, "DNI. _______________, ha dado cumplimiento con los")
    c.drawString(350, 410, dni)
    c.drawString(340, 370, "requisitos de aprobación del curso de")
    c.drawString(240, 320, "________________________________________________________________")
    c.drawString(340, 320, carrera)
    c.drawString(250, 280, "dictado por Aula Taller Capacitaciones con el aval académico de")
    c.drawString(250, 250, "la Universidad de Flores con una carga horaria de ___ horas reloj.")
    c.drawString(650, 250, carga_horaria)
    c.setFont('Vera', 12)
    c.drawString(340, 210, "Se extiende el presente Certificado que así lo acredita,")
    c.drawString(320, 190, "en la Ciudad Autónoma de Buenos Aires, República Argentina,")
    c.drawString(355, 170, "a los __ días del mes de ____________ del año ____.")
    c.drawString(385, 170, dia)
    c.drawString(505, 170, mes)
    c.drawString(625, 170, anio)
 

    #Firmas - Lineas
    c.line(x + 30, 100, x + 200, 100)
    c.line(x + 210, 100, x + 380, 100)
    c.line(x + 390, 100, x + 560, 100)

    #Firmas - texto Medio
    c.setFont('Vera', 8)
    c.drawString(470, 80, "Lic. Natalia Arias")
    c.drawString(430, 70, "Secretaria Regional de Vinculación.")
    c.drawString(490, 60, "UFLO")

    #Firmas - texto Izquierda
    c.setFont('Vera', 8)
    c.drawString(290, 80, "Lic. Natalia Arias")
    c.drawString(250, 70, "Secretaria Regional de Vinculación.")
    c.drawString(310, 60, Sede)

    #Firmas - texto Derecha
    c.setFont('Vera', 8)
    c.drawString(650, 80, "Lic. Natalia Arias")
    c.drawString(610, 70, "Secretaria Regional de Vinculación.")
    c.drawString(670, 60, Sede)

    c.save() 