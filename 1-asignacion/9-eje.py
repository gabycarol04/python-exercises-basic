# Ejercicio 9
# Escribí un programa que solicite al usuario ingresar tres números para luego mostrarle el promedio de los tres.

numero_1=float(input("Ingresar el primer número: "))
numero_2=float(input("Ingresar el segundo número: "))
numero_3=float(input("Ingresar el tercero número: "))

promedio=round((numero_1+numero_2+numero_3)/3,2)

print("El promedio es:",promedio)