# Ejercicio 5
# Para tributar un determinado impuesto se debe ser mayor de 16 años y tener unos ingresos iguales o superiores a 1000 € mensuales. Escribir un programa que pregunte al usuario su edad y sus ingresos mensuales y muestre por pantalla si el usuario tiene que tributar o no.

import sys

edad=int(input("Ingrese su edad: "))
ingreso=float(input("Ingrese su ingreso mensual: "))

if edad < 18:
    print("No tiene que tributar")
    sys.exit()

if ingreso < 1000:
    print("No tiene que tributar")
else:
    print("Si tiene que tributar")
