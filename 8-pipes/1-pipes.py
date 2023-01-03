# 5.Crear un programa que cree dos hilos. Un hilo va a estar generando números aleatorios de 1 a 100, el otro hilo va a estar revisando que valores se generan. Al hilo que revisa, se le pasa cómo argumento un valor que en caso de aparecer en el hilo que genera números, finaliza el programa. Por ultimo se imprime en pantalla la cantidad de números generados.
# 6.Implemente el punto anterior con pipes

import multiprocessing
import random
import threading

def enviar(connection):
    i=0
    for i in range(10):
        value = random.randint(1,100)
        connection.send(value)
    connection.send(None)

def receptor(connection):
    while True:
        numero=connection.recv()
        if (numero == None):
            break
        print("Recibido numero",numero)

conn1,conn2= multiprocessing.Pipe()

emisario=threading.Thread(target=enviar,args=(conn2,))
destino=threading.Thread(target=receptor,args=(conn1,))

emisario.start()
destino.start()