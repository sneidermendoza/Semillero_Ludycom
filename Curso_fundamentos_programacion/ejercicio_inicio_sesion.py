user = "sneider"
password = 12345
acceso = False
intento = 0
print("¡¡Inicio de sesion!!")

print("Ingrese usuario y contraseña")


while acceso == False :
    usuario = input("usuario: ")
    contrasena = input("contraseña: ")
    if usuario != user and contrasena != password:
        print("Usuario o contraceña invalido")
        intento += 1
        print("quieres restablecer la contraseña?")
        si_no = input("Si / No: ")
        si_no = si_no.lower()
        if si_no == "si":
            while True:
                print("Restablecer Contraseña")
                c1 = input("Contraseña: ")
                c2 = input("Confirmar Contraceña")
                if c1 != c2:
                    print("Contraseñas no coinciden, intentalo de nuevo")
                else:
                    print("Contraseña Cambiada")

                    print("Ingrese usuario y contraseña")
                    break
        elif si_no == "no":
            if intento == 2:
                print("exediste el limite de intentos, espera 10 minutos para volver a intentar")
                acceso = True
    else:
        print("!!sesion iniciada¡¡")
        acceso = True




