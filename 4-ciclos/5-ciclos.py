# Ejercicio 5
# Escribir un programa en el que se pregunte al usuario por una frase y una letra, y muestre por pantalla el número de veces que aparece la letra en la frase.

frase=input("Ingrese una frase: ")
letra=input("Ingrese una letra: ")

cont=0
for x in frase:
    if x == letra:
        cont+=1

print("La letra",letra,"se encuentra",cont,"veces en la frase")