import mysql.connector

# Crear conexión a una base de datos específica
conexion=mysql.connector.connect(host='localhost',user="admin",passwd="admin123", database="bd_prueba")
cursor=conexion.cursor()

nombre=input("Ingrese nombre: ")
apellido=input("Ingrese apellido: ")
id=input("Ingrese id: ")

# Ejecutar comandos en la base de datos a través del cursor
# Un cursor regularmente devuelve un arreglo
cursor.execute("select * from pruebas")
cursor.execute( f"insert into prueba(idprueba,nombre,apellido) values(\"{id}\",\"{nombre}\",\"{apellido}\") ")

#Se debe guardar en el programa
conexion.commit()

# Cerrar la conexión para ahorrar recursos
conexion.close()
