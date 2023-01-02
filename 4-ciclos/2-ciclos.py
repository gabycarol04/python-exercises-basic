# Ejercicio 2
# Escribir un programa que pregunte al usuario su edad y muestre por pantalla todos los años que ha cumplido (desde 1 hasta su edad).

edad=int(input("Ingrese su edad: "))

cont=0
while cont < edad:
    print(cont+1)
    cont+=1