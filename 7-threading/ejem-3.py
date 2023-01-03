# Enviar argumentos con hilos

import threading

def contar(numero_hilo,**datos):
    contador=datos['inicio']
    incremento=datos['incremento']
    limite=datos['limite']

    while contador < limite:
        contador+=incremento
        print(
            f" Hilo :{numero_hilo} contador : {contador}"
        )

numero_hilos=4

for num in range(numero_hilos):
    # Creación de Hilo
    hilo=threading.Thread(name='hilo %s' %num,target=contar,args=(num,),kwargs={'inicio':0,'incremento':1,'limite':10})   
    # Ejecutar Hilo
    hilo.start()