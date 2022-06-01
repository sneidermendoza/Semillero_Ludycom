"""
Ejercicio para buscar el top.
Recorrer un array unimodal y buscar cual es el top del mismo 
"""

v=[1,2,4,4,5,6,4,3,2]
def top(v,l,r):
    if l + 1 >= r: return max(v[l], v[r])
    else:
        m = (l+r) // 2
        if v[m] < v[m+1]: return top(v,m+1,r)

        elif v[m-1] > v[m]: return top(v,l,m-1)

        else:
            return v[m]
print(top(v,0,(len(v)-1)))
