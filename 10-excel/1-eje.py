# Ingresar datos a un excel vacio

import openpyxl

def ingresar_datos():
    print("----------- Agregando columnas ----------")
    hoja=excelDocument['Hoja1']
    celdas=hoja['C6':'E10']

    titulo=["Nombre completo","Ciudad","Teléfono"]
    trabajador=[
        ["María Gonzalez", "Panamá", "6638103"],
        ["Rodrigo Peréz", "Colón", "6623714"],
        ["Diamond Zung", "Corea", "5512389"],
        ["Katsuki Onodera", "Japón", "6612389"]
    ]

    numero_fila=0
    for fila in celdas:
        numero_columna=0
        for column in fila:
            if numero_fila==0:
                column.value=titulo[numero_columna]
                excelDocument.save('trabajadores.xlsx')
            else:
                aux_fila=numero_fila-1
                column.value=trabajador[aux_fila][numero_columna]
                excelDocument.save('trabajadores.xlsx')
            numero_columna+=1
        numero_fila+=1

def mostrar_datos():
    print("----------- Mostrar columnas ----------")
    hoja=excelDocument['Hoja1']
    celdas=hoja['C6':'E10']

    for fila in celdas:
        for column in fila:
            print(column.value)

test=[
    ["María Gonzalez", "Panamá", "6638103"],
    ["Rodrigo Peréz", "Colón", "6623714"],
    ["Diamond Zung", "Corea", "5512389"],
    ["Katsuki Onodera", "Japón", "6612389"]
]

try:
    excelDocument = openpyxl.load_workbook('trabajadores.xlsx')
except FileNotFoundError:
    print("No se encontro el archivo")
else:
    ingresar_datos()
    mostrar_datos()
