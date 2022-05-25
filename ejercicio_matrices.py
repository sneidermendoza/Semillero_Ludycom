#TUPLAS no se le puede añadir elementos o modificar

paises = ("argentina", "autralia", "belgica", "brasil", "chile", "egipto", "francia", "panama", "sudafrica", "turquia", "tunez")

print(len(paises))
print(paises[3])
print(paises[0])
#print(paises[-2]) este daria error por que no existe esta posicion
#print(paìses[4]) esto daria error por que la valiable con tilde no existe
#print(paises[15]) este daria error por que no existe esta posicion
print(paises[8])
#print(paises[13]) este daria error por que no existe esta posicion

print("-".join(paises))

print("////////////////////////////////////////////////////////////////////////")


# ARRAY se puede coleccionar diferentes tipos de datos y se puede modificar añadir o eliminar

paises2 = ["panama", "egipto", "argentina"]

paises2.append("francia")
print(paises2)

paises2.remove(paises2[1])
print(paises2)

paises2.append("australia")
print(paises2)

paises2.sort()
print(paises2)

paises2.append("brasil")
print(paises2)


