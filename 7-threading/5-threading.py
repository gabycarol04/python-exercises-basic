# 5..Crear un programa que cree dos hilos. Un hilo va a estar generando números aleatorios de 1 a 100, el otro hilo va a estar revisando que valores se generan. Al hilo que revisa, se le pasa cómo argumento un valor que en caso de aparecer en el hilo que genera números, finaliza el programa. Por ultimo se imprime en pantalla la cantidad de números generados.


import threading
import random
import time

def generar_numeros():
    global numero
    contador=0
    while numero < 200:
        numero_random = random.randint(1,100)
        numero+=numero_random
        contador+=1
        print(
            f" Hilo :{threading.current_thread().getName} Número : {numero}"
        )
        time.sleep(0.3)
    print(f"Cantidad de numeros creados: {contador}")

def revisar_valor():
    global numero
    cont=0
    while cont < 500:
        print(f"El valor es: {numero}")
        cont+=1
        time.sleep(0.1)

numero=0

hilo1 = threading.Thread(name='Hilo Revisar',target=revisar_valor,daemon=True)
hilo2 = threading.Thread(name='Hilo Generar',target=generar_numeros)

hilo1.start()
hilo2.start()