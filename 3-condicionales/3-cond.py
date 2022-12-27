# Ejercicio 3
# Escribir un programa que pida al usuario dos números y muestre por pantalla su división. Si el divisor es cero el programa debe mostrar un error.

import sys

dividendo=int(input("Ingrese el dividendo: "))
divisor=int(input("Ingrese el divisor: "))

if divisor <= 0:
    print("El divisor no es válido")
    sys.exit()

division=round(dividendo/divisor)

print("El resultado es:",division)
