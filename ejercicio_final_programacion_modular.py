print("""
Programa para calcular el area de una figura geometrica
""")
def calcular_area_circulo():
        radio = float(input("Ingrese el radio: "))
        area = (radio* radio) * 3.14159
        print(f"El areaes: {area}")

def calcular_area_triangulo():
        base = float(input("Ingrese la medida de la base: "))
        altura = float(input("Ingrese la medida de la altura: "))
        area = (base* altura) / 2
        print(f"El area es: {area}")

opcion = int(input("Por favor seleccione una opcion:\n-> 1-(Circulo)\n-> 2-(Triangulo)\n="))

while True:
    if opcion == 1:
        calcular_area_circulo()
        pass
    opcion = int(input("Por favor seleccione una opcion:\n-> 1-(Circulo)\n-> 2-(Triangulo)\n="))   
    if opcion == 2:
        calcular_area_triangulo()
        pass
    opcion = int(input("Por favor seleccione una opcion:\n-> 1-(Circulo)\n-> 2-(Triangulo)\n="))
    if opcion != 1 and opcion != 2:
        print("~~Opcion invalida elige de nuevo~~")
        opcion = input("Por favor seleccione una opcion:\n-> 1-(Circulo)\n-> 2-(Triangulo)\n=")



   
    
    