# Se declara y ejecutan dos hilos que ejecutan una misma función (target)

import threading

def contar():
    contador=0
    while contador <=20:
        contador+=1
        print(
            f" Hilo :{threading.current_thread().getName()} con identificador: {threading.current_thread().ident} contador : {contador}"
        )

# Creación de Hilo
hilo1=threading.Thread(target=contar)   
hilo2=threading.Thread(target=contar)

# Ejecutar Hilo
hilo1.start()
hilo2.start()
