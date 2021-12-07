import sqlite3
from sqlite3 import Error
import xlrd
from xlrd import sheet
from openpyxl import load_workbook


# database connection
def sql_connection():
    try:
        con = sqlite3.connect('db.sqlite3')
        print("Conectado")
        return con
    except Error:
        print(Error)


def sql_insert(con, array_test):
    cursorObj = con.cursor()
    for value in array_test:
        sql = 'INSERT INTO certificado_datafile ("nombre","apellido","dni","sede","carrera","horas","dia","mes","anio","firmaNameI","firmaPuestoI","firmaNameD","firmaPuestoD") VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")' \
              % (value['Nombre'], value['Apellido'], value['DNI'], value['Sede'], value['Curso'], value['Horas'],
                 value['Dia'], \
                 value['Mes'], value['Anio'], value['Nombre Iz'], value['Puesto Iz'], value['Nombre D'],
                 value['Puesto D'])
        cursorObj.execute(sql)
    con.commit()


# filepath = "./aulaTaller.xlsx"

def main(file):
    filepath = 'certificado/static/docs/' + str(file.archivo)
    wb = load_workbook(filename=filepath)
    ws = wb.active
    array = []
    ws.delete_rows(1)
    fila = 1
    for row in ws.values:
        valores = {
            "row": fila,
            "Nombre": row[0],
            "Apellido": row[1],
            "DNI": row[2],
            "Sede": row[3],
            "Curso": row[4],
            "Horas": row[5],
            "Dia": row[6],
            "Mes": row[7],
            "Anio": row[8],
            "Nombre Iz": row[9],
            "Puesto Iz": row[10],
            "Nombre D": row[11],
            "Puesto D": row[12],
        }
        array.append(valores)
        fila += 1
    con = sql_connection()
    sql_insert(con, array)

    return array
