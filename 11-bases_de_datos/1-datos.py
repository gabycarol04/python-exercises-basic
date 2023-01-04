import mysql.connector

# Crear conexión a la base de datos
conexion=mysql.connector.connect(host='localhost',user="admin",passwd="admin123")
cursor=conexion.cursor()

# Ejecutar comandos en la base de datos a través del cursor
# Un cursor regularmente devuelve un arreglo
cursor.execute("show databases")
for base in cursor:
    print(base)

# Cerrar la conexión para ahorrar recursos
conexion.close()
