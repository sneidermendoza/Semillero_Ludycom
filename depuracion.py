def factorial():
    resultado = 1
    print("factorial de un numero")
    numero = int(input("Ingrese un numero: "))

    for i in range(1, numero + 1):
        resultado *= i

    print(resultado)
    return factorial()

factorial()