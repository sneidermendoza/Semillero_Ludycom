def factorial():
    resultado = 1
    print("factorial de un numero")
    try:
     numero = int(input("Ingrese un numero: "))
     if numero < 0:
        print("Ingresaste un numero negativo.")
        pass
    except:
        print("No se puede ingresar letras o simbolos, intentalo de nuevo->")
        return factorial()
    for i in range(1, numero + 1):
        resultado *= i

    if resultado != 1:
        print(resultado)
    return factorial()

factorial()