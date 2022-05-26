def multiplicar_numero_cuadrado():

    print("~~multiplicar un numero al cuadrado~~")

    try:
        numero = int(input("Ingrese un numero: "))
        resultado = (numero * numero)
        print(resultado)
    except:
        print("No se permiten letras o simbolos")
        return multiplicar_numero_cuadrado()



multiplicar_numero_cuadrado()