# Ejercicio 1
# Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10 veces.

palabra=input("Ingrese una palabra: ")

cont=0
while cont < 10:
    print(cont+1,".",palabra)
    cont += 1