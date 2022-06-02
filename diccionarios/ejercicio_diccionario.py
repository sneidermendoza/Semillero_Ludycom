from audioop import reverse
import collections

d = {2:13, 1:9, 4:25, 3:0} # Diccionario inicial
print(f"Diccionario inicial: {d}")
print("------------------------")

d[int(input("ingrese valor:"))]=(int(input("ingrese clave:"))) # Ingresar por consola elementos a un diccionario
d[5] = 30 # Ingresar manualmente elementos a un diccionario
d = d
print(f"Diccionario con los nuevos ingresos: {d}")
print("------------------------")

s=len(d) # Longitud de un diccionario
print(f"La longitud del diccionario es: {s}")
print("------------------------")

p = list(d.items()) # Convertir a lista un diccionario
print(f"Diccionario convertido a lista.{p}")
print("------------------------")

print("Recorrer e imprimir los elemntos del diccionario")
for clave,valor in d.items(): # Iterar los elementos de un diccionario
    print(f"{clave}:{valor}")
print("------------------------")

result = collections.OrderedDict(sorted(d.items())) # Ordenar los elementos de un diccionaro en forma ascendente, por su clave
print(f"Diccionario ordenado de manera accendente por su clave:\n{result}")
print("------------------------")

result2 = list(result)
print(result2)



