# Ejercicio 6
# Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta que el usuario escriba “salir” que terminará.

cont=0
print("Ingrese \"salir\" para salir del programa")

while cont < 1:
    frase=input("Ingrese una frase: ")
    if frase == "salir":
        print("Bye")
        break
    else:
        print(frase)
