calificaciones = []

print(">>>>>>>DETERMINE LA CALIFICACION MAS ALTA<<<<<<<<")
print("\n")


calificacion = float(input("Ingrese calificacion o (0) para terminar:  "))

while calificacion != 0:
    if calificacion == 0:
        break
    else:
        calificaciones.append(calificacion)
        calificacion = float(input("Ingrese calificacion o (0) para terminar:  "))

print(f"Las calificacioness ingresadas son: {calificaciones}")
print("--------------------------------------")

highest_rating = 0
for i in calificaciones:
    if i > highest_rating:
        highest_rating = i

print(f"La calificacion mas alta es {highest_rating}")
    