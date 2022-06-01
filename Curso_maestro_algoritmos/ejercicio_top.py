# v  = [1,2,3,4,5,6,7,8,9]

# def par_impar(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False

# def top(v):
#     mitad = len(v) // 2
#     if par_impar(mitad):
#         mitad +1
#     else:
#         mitad

#     medio = v[mitad]
    

# print(top(v))
v=[9,18,7,6,8,30,24,]
def top(v,l,r):
    if l + 1 >= r: return max(v[l], v[r])
    else:
        m = (l+r) // 2
        if v[m] < v[m+1]: return top(v,m+1,r)

        elif v[m-1] > v[m]: return top(v,l,m-1)

        else:
            return v[m]
print(top(v,0,(len(v)-1)))
