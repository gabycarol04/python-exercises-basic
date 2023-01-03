# Busca un excel que no existe

import openpyxl

try:
    excelDocument = openpyxl.load_workbook('samples.xlsx')
except FileNotFoundError:
    print("No se encontro el archivo")
else:
    print(excelDocument)
