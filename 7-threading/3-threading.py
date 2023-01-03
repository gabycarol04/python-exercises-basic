# 3.Crear 3 hilos que sumen cada uno un valor aleatorio en una variable hasta llegar a 5000. Mostrar por pantalla cuanto suma cada uno.

import threading
import random
import os

def suma():
    global contador
    while contador <= 5000:
        contador+=int(random.random()*10)
        print(f"Hilo: {threading.current_thread().getName} Suma Actual: {contador}")

contador=0
numero_hilos=4

for num in range(numero_hilos):
    hilo=threading.Thread(name='Sumador %s' %num,target=suma)
    hilo.start()