# Ejercicio 4
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña correcta.

contraseña=input("Ingrese su contraseña: ")

cont=0
while cont < 1:
    validar=input("Ingrese su contraseña nuevamente: ")
    if validar == contraseña:
        print("Hemos guardado su contraseña")
        cont += 1
    else:
        print("Su contraseña no coincide")
