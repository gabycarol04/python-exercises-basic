# 1.Crea una función llamada Contador que contenga un atributo que sea un contador, otro que sea el nombre del hilo y otro que sea el limite del contador, es decir, donde debe acabar. Crea 6 contadores y ejecútalos. Debe mostrar por pantalla el nombre de cada hilo y en que cuenta va

import threading

def contador(cont,hilo,limit):
    print(hilo)
    while cont < limit: 
        print(
            f" Hilo :{threading.current_thread().getName()} con identificador: {threading.current_thread().ident} contador : {cont+1}"
        )
        cont+=1

cont=0
limit=6
numero_hilos=3

for num in range(numero_hilos):
    # Creación de Hilo
    nombre_hilo='hilo %s' %num
    hilo=threading.Thread(name='hilo %s' %num,target=contador(cont,nombre_hilo,limit))   
    # Ejecutar Hilo
    hilo.start()
