# Guardar un valor

import openpyxl

try:
    excelDocument = openpyxl.load_workbook('sample.xlsx')
except FileNotFoundError:
    print("No se encontro el archivo")
else:
    hoja=excelDocument['Hoja1']
    palabra=hoja['C6']
    print(palabra.value)

    hoja['C7']="Posicion"
    excelDocument.save('sample.xlsx')
finally:
    print("Cerrando programa...")