import sqlite3
from sqlite3 import Error
import xlrd
from xlrd import sheet

#database connection
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
        sql = 'INSERT INTO certificado_datafile ("nombre","apellido","dni","sede","carrera","horas","dia","mes","anio","firmaNameI","firmaPuestoI","firmaNameD","firmaPuestoD") VALUES ("%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s","%s")'\
            % (value['Nombre'],value['Apellido'],value['DNI'],value['Sede'],value['Curso'],value['Horas'],value['Dia'],\
               value['Mes'],value['Anio'],value['Nombre Iz'],value['Puesto Iz'],value['Nombre D'],value['Puesto D'])
        #print(sql)
        cursorObj.execute(sql)
    con.commit()

filepath = "./aulaTaller.xlsx"

def main(filepath):

    openFile  = xlrd.open_workbook(filepath)
    sheet = openFile.sheet_by_name("Hoja1")
    array_test = []
    for i in range (1, sheet.nrows):
        valores = {
            "Nombre": sheet.cell_value(i,0),
            "Apellido": sheet.cell_value(i,1),
            "DNI": sheet.cell_value(i,2),
            "Sede": sheet.cell_value(i,3),
            "Curso": sheet.cell_value(i,4),
            "Horas": sheet.cell_value(i,5),
            "Dia": sheet.cell_value(i,6),
            "Mes": sheet.cell_value(i,7),
            "Anio": sheet.cell_value(i,8),
            "Nombre Iz": sheet.cell_value(i,9),
            "Puesto Iz": sheet.cell_value(i,10),
            "Nombre D": sheet.cell_value(i,11),
            "Puesto D": sheet.cell_value(i,12)
        }
        array_test.append(valores)
    

    con = sql_connection()
    sql_insert(con, array_test)

#print(sheet.nrows)
#print(sheet.ncols)
#print(array_test)