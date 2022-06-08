"""Escriba una función recursiva eficiente que devuelva la posición de x 
en el subvector v [left..right]. La función debe devolver −1 
si x no pertenece a v [left..right] o si left> right.
Condición previa:
El vector v se ordena en orden estrictamente creciente. 
Además, tenemos 0 ≤ izquierda ≤ tamaño de v y −1 ≤ derecha < tamaño de v.
Construya la siguiente función: 
int position(double x, const vector<double>& v, int left, int right)
"""
n = int(input("Numero de elementos\n-> "))
lista = []
for i in range(n):
    a = float(input(f"Ingrese los elementos del  vector en orden extrictamente creciente\n{i+1})-> "))
    lista.append(a)
x = float(input("Ingrese elemento a buscar\n-> "))

def position(x, v, left, right):
    if left > right: return -1
    
    posicion = (left + right) // 2
    if x > v[posicion]: return position(x, v, posicion +1, right)
    if x < v[posicion]: return position(x, v, left, posicion -1)
    return posicion




resultado = position(x,lista,0, n-1)
print(f"el elemento >> {x} << se encuentra en la posicion >> {resultado+1} <<")
