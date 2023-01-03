# 2.Crear dos hilos que corran una carrera, existe una probabilidad del 25% de que no avance el hilo. Implementar que se muestre por pantalla cual hilo llego primero a la meta y que se vea todo el tiempo cuanto a avanzado.

import threading
import time
import random

ganador=False

def avanzar(meta):
    global ganador
    avance=0
    while not ganador:
        if(random.randint(1,100)>25):
           
            avance+=1
            print(threading.current_thread().getName(),"ha avanzado ",avance)
            if(avance>=meta):
                if(not ganador):
                    print(threading.current_thread().getName(),"ha ganado")
                    ganador=True
            time.sleep(0.2)
        else:
            print(threading.current_thread().getName(),"no avanzo")
            time.sleep(0.2)

meta=15
hilo1=threading.Thread(name="Corredor 1",args=(meta,),target=avanzar)
hilo2=threading.Thread(name="Corredor 2",args=(meta,),target=avanzar)
hilo1.start()
hilo2.start()