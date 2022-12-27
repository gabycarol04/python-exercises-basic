# Ejercicio 12
# Una panadería vende barras de pan a $3.49 cada una. El pan que no es del día tiene un desceutno del 60%. Escribir un Programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barrra de pan, el descuento que se le hace por no ser fresca y el coste final total.

pan=3.49
descuento=0.6

vendidas=float(input("Barras de pan vendidas: "))
costo=round((pan*vendidas)*descuento,2)

print("Precio habitual:",pan)
print("Descuento del pan:",descuento*100,"%")
print("Costo total:",costo)