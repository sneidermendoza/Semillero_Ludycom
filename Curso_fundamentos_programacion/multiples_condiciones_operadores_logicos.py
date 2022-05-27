print("Condiciones para descuento, si es mujer y es mayor de 60 años ")

print("···················")
edad =  int(input("Por favor ingrese la edad:\n"))
opcion = int(input("Es mujer?\nEligeuna opcion: 1:Si | 2:NO \n"))

while opcion != 1 or opcion != 2:
    
    if opcion == 1:
        mujer = True
        break
    elif opcion == 2:
        mujer = False
        break
    else:
        print("ingresaste una opcion no validad, vuelvelo a intentar")
        opcion = int(input("es mujer?\nEligeuna opcion: 1:Si | 2:NO \n"))

if mujer == True or edad >= 60:
    print("Se aplica descuento")
else:
    print("No se aplica descuento")