# Usualmente los hilos se declaran dentro de ciclos

import threading

def contar():
    contador=0
    while contador <=50:
        contador+=1
        print(
            f" Hilo :{threading.current_thread().getName()} con identificador: {threading.current_thread().ident} contador : {contador}"
        )

numero_hilos=4

for num in range(numero_hilos):
    # Creación de Hilo
    hilo=threading.Thread(name='hilo %s' %num,target=contar)   
    # Ejecutar Hilo
    hilo.start()
