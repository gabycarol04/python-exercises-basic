# Se esta pidiendo un indice del arreglo que no existe

variable=[8,6,9,8,7]

try:
    variable[2]
except IndexError:
    print("Se salio del arreglo")
else:
    print(variable[2])
