import openpyxl
import time
import multiprocessing
import threading

def logs(conn):
    file=open('logs.txt','w')
    while True:
        info=conn.recv()
        if info!= None:
            file.write(info+"\n")
        else:
            break
    file.close()

def cambiarArchivo():
    global archivo
    global documento
    global nombreHoja
    global hoja
    try:
        nameArchivo=input("Ingrese el nombre del archivo: ")
        documentoAux=openpyxl.load_workbook(f"{nameArchivo}.xlsx")
        nameHoja=input("Ingrese nombre de la hoja de trabajo: ")
        hojaAux=documentoAux[nameHoja]
    except FileNotFoundError:
        print("ERROR- Archivo no encontrado")
    except KeyError as e:
        print("ERROR- Hoja no encontrada")
    else:
        archivo=nameArchivo
        documento=documentoAux
        nombreHoja=nameHoja
        hoja=hojaAux
        print("Cambio a el archivo",archivo,"en la hoja",nombreHoja)

def cambiarHoja():
    global nombreHoja
    global hoja
    try:
        nameHoja=input("Ingrese nombre de la hoja de trabajo: ")
        hojaAux=documento[nameHoja] 
    except KeyError as e:
        print("ERROR- Hoja no encontrada")
    else:
        nombreHoja=nameHoja
        hoja=hojaAux
def crear():
    try:
        posicion=input("Ingrese la posicion de la celda: ").upper()
        conn2.send(posicion)
        valor=hoja[posicion].value
        hoja[posicion]=input("Ingrese informacion a almacenar: ")
        conn2.send(hoja[posicion].value)
        print(f"Informacion almacenada: {hoja[posicion].value}")
        documento.save(f"{archivo}.xlsx")
    except PermissionError:
        hoja[posicion]=valor
        print("Por favor cierre el excel- Informacion no almacenada")
    except AttributeError:
        print("Celda invalida")
def editar():
    try:
        posicion=input("Ingrese la posicion de la celda: ").upper()
        conn2.send(posicion)
        valor=hoja[posicion].value 
        print("Valor actual celda: ",valor)
        nuevo=input("Ingrese el nuevo valor de la celda: ")
        conn2.send(nuevo)
        print(f"Cambio: {valor} --> {nuevo}")
        descicion=input("Confirmar cambio? y/n:")
        conn2.send(descicion)
        if(descicion=="y"):
            hoja[posicion]=nuevo
            documento.save(f"{archivo}.xlsx")
            print("Informacion almacenada")
        else:
            print("Accion cancelada")
    except PermissionError:
        hoja[posicion]=valor
        print("Por favor cierre el excel- Informacion no almacenada")
    except AttributeError:
        print("Celda invalida")
def eliminar():
    try:
        posicion=input("Ingrese la posicion de la celda: ").upper()
        conn2.send(posicion)
        valor=hoja[posicion].value
        print("Valor de la celda: ",valor)

        descicion=input("Confirmar eliminar? y/n:")
        conn2.send(descicion)
        if descicion=="y":
            hoja[posicion]=None
            documento.save(f"{archivo}.xlsx")
            print("Celda eliminada")
        else:
            print("Accion cancelada")
    except PermissionError:
        hoja[posicion]=valor
        print("Por favor cierre el excel- Informacion no almacenada")
    except AttributeError:
        print("Celda invalida")
def visualizar():
    try:
        posicion=input("Ingrese la posicion de la celda: ").upper()
        conn2.send(posicion)
        print(f"Valor de la celda: {hoja[posicion].value}")
    except AttributeError:
        print("Celda invalida")
try:
    conn1,conn2=multiprocessing.Pipe()
    hilo=threading.Thread(target=logs, args=(conn1,))
    hilo.start()
    archivo=input("Ingrese el nombre del archivo: ")
    conn2.send(archivo)
    documento=openpyxl.load_workbook(f"{archivo}.xlsx")
    nombreHoja=input("Ingrese nombre de la hoja de trabajo: ")
    conn2.send(nombreHoja)
    hoja=documento[nombreHoja]

except FileNotFoundError:
    print("ERROR- Archivo no encontrado")
except KeyError as e:
    print("ERROR- Hoja no encontrada")
else:
    while True:
        time.sleep(1.5)
        mensaje="""
        ¿Que desea hacer?

        1-Crear celda
        2-Editar celda
        3-Eliminar celda
        4-Visualizar celda
        5-Cambiar archivo
        6-Cambiar hoja


        -exit
        """
        print(mensaje)

        accion=input()
        conn2.send(accion)

        if accion=="1":
            print("Creando...")
            crear()
        elif accion=="2":
            editar()
        elif accion=="3":
            eliminar()
        elif accion=="4":
            visualizar()
        elif accion=="5":
            cambiarArchivo()
        elif accion=="6":
            cambiarHoja()

        elif accion.lower()=="exit":
            print("Saliendo....")
            conn2.send(None)
            break
        else:
            print("Ingrese un valor valido")