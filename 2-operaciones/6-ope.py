# Ejercicio 6
# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha_completa=input("Ingrese su fechaa de nacimiento con este formato dd/mm/aaaa: ")

fecha=fecha_completa.split("/")

cont=0
while cont < len(fecha):
    if len(fecha[cont]) < 2:
        fecha[cont]="0"+fecha[cont]
    cont=cont+1

print("Día:",fecha[0],"Mes:",fecha[1],"Año:",fecha[2])

