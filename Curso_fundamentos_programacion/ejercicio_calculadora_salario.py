print(">>>Calculadora de salario<<<")
print("*******************************************")
empleado = input("Por favor ingrese nombre del empleado:\n")
salario = float(input("Por favor ingrese su salario por dia: \n$"))
dias_trabajo = int(input("Por favor ingrese los dias trabajados: \n"))

sueldo = salario * dias_trabajo

print("__--__--__--__--__--__--__--")

print(f"Empleado: {empleado}\nSalario: {salario}\nDias de trabajo: {dias_trabajo}\nSueldo: {sueldo} ")


