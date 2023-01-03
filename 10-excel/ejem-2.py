# Imprime el valor en una celda

import openpyxl

try:
    excelDocument = openpyxl.load_workbook('sample.xlsx')
except FileNotFoundError:
    print("No se encontro el archivo")
else:
    hoja=excelDocument['Hoja1']
    palabra=hoja['C6']
    print(palabra.value)
finally:
    print("Cerrando programa...")