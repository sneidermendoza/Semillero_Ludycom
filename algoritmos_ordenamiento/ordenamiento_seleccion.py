"""
Algoritmo de ordenamiento por seleccion,
se ordena un array(lista) en forma ascendente
"""
def ordenamiento_seleccion(lista):
    for i in range(0, len(lista)):
        minimo = i

        for j in range(i+1, len(lista)):
            if lista[minimo] > lista[j]:
                minimo = j

        temporal = lista[i]
        lista[i] = lista[minimo]
        lista[minimo] = temporal
    return lista

lista=[20, 30, 25, 10, 8, 98, 1, 6, 4]
a = ordenamiento_seleccion(lista)
print(a)
