# Ejercicio 8
# Escribir un programa que solicite al usuario ingresar la cantidad de kilómetros recorridos por una motocicleta y la cantidad de litros de combustible que consumió durante ese recorrido. Mostrar el consumo de combustible por kilómetro.

kilometros=float(input("Ingrese la cantidad de kilómetros recorridos: "))
combustible=float(input("Ingrese la cantidad de combustible consumido: "))

consumo=combustible/kilometros

print("Cantidad de combustible consumido por kilómetro:",consumo)