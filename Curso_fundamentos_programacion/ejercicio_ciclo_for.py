nombres = ["sneider", "brando", "alexander", "juan"]

for i in nombres:
    print(i)

resultado = 0


print("---------------------")

for i in range(11):
    if i != 0:
        resultado += i
        i += 1

print(resultado)

print("---------------------")


calificaciones = [90.5, 87.4, 65.6, 40.57]
suma = 0

for i in calificaciones:
    suma += i

print(suma / len(calificaciones))
