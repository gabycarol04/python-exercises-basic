# Ejercicio 5
# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo=input("Ingrese su correo: ")

correo_base=correo.split("@")
correo_nuevo=correo_base[0]+"@ceu.es"

print("Su nuevo correo es:",correo_nuevo)

