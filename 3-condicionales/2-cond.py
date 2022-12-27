# Ejercicio 2
# Escribir un programa que almacene la cadena de caracteres contraseña en una variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida por el usuario coincide con la guardada en la variable sin tener en cuenta mayúsculas y minúsculas.

contraseña=input("Ingrese su contraseña: ")
confirmacion=input("Confirme su contraseña: ")

if contraseña == confirmacion:
    print("Su contraseña se ha guardado")
else:
    print("Su contraseña no coincide")