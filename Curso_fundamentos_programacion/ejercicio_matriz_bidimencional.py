"""
Crear una matriz bidimencional
"""
from random import *

columnas = int(input("ingrese el numero de filas\n-> "))
filas = int(input("ingrese el numero de columnas\n-> "))

matriz = [[randint(1,100) for i in range(filas)] for j in range(columnas)]

for f in matriz:
    print(f)

