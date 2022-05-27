edad = int(input("Ingrese la edad: "))

if  edad < 1 or edad > 125:
    print("Edad invalida")
elif edad < 18:
    print("Eres menor de edad")
elif  edad >= 18 or edad < 59:
    print("Mayor de edad")
else:
    print("Eres de la tercera edad")