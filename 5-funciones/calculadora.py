# Taller
# Para la aplicación de los conceptos aprendidos dentro de esta introduccion a python vamos a realizar un taller que integre todos estos conceptos.

# Se requiere una calculadora que permita hacer las 4 operaciones basicas, que pida los numeros y el operador por consola y no pare de realizar las operaciones hasta que se diga la palabra "exit".

def calculadora(numero1,numero2,operador):
    if (operador=='+'):
        print("El resultado de su operación es: ",numero1+numero2)
    elif (operador=='-'):
        print("El resultado de su operación es: ",numero1-numero2)
    elif (operador=='*'):
        print("El resultado de su operación es: ",numero1*numero2)
    elif (operador=='/'):
        print("El resultado de su operación es: ",numero1/numero2)
    else:
        print("El operador no es válido")

cont=0
while cont < 1:
    print("---- Calculadora --------------------")

    numero1=int(input("Ingrese el primer número entero: "))
    numero2=int(input("Ingrese el segundo número entero: "))
    operador=input("Ingrese el operador: ")

    calculadora(numero1,numero2,operador)

    salir=input("Para salir de la aplicación escriba \"exit\", sino cualquier otra tecla: ")

    if salir == 'exit':
        cont+=1
    

