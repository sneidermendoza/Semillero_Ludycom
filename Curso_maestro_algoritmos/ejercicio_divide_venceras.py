"""
Ejercicio de ordenamiento.
Algoritmo para ordenar un arreglo aplicando,
divide y venceras con recursividad 
"""

def merge_sort(A,p,r):
    if p < r:
        q = (p+r) // 2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    derecha = A[p:q+1]
    izquierda = A[q+1:r+1]

    izquierda.append(float("inf"))
    derecha.append(float("inf"))
    
    i = 0
    j = 0
    k = p

    while k <= r and j < len(derecha) and i < len(izquierda):
        if izquierda[i] > derecha[j]:
            A[k] = derecha[j]
            j += 1
        else:
            A[k] = izquierda[i]
            i += 1

        k += 1

lista_A = [5,2,4,7,1,3,2,6]
merge_sort(lista_A,0,7)
print(lista_A)