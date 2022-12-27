# Ejercicio 1
# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

depositado=float(input("Ingrese el monto depositado: "))
interes=0.4

mes_1=round(depositado+(depositado*0.4),2)
mes_2=round(mes_1+(mes_1*0.4),2)
mes_3=round(mes_2+(mes_2*0.4),2)

print("Primer mes:",mes_1,"Segundo mes:",mes_2,"Tercer mes:",mes_3)

