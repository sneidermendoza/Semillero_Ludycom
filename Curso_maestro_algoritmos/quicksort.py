lista = [4,9,2,1,6,3,8]

def quick_sort(l):
    
    if len(l) < 1: return []
    izq = []
    der = []
    pivote = l[0]
    for i in range(1,len(l)):
        if l[i] < pivote:
            izq.append(l[i])
        else: der.append(l[i])
    return quick_sort(izq)+[pivote]+quick_sort(der)

print(quick_sort(lista))


