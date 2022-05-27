""" 
Escribir una funcion que permita calcular el total de impuestos que debe pagar un trabajador,
en base a su salario y al porcentage que paga de impuestos.
 """
def total_impuesto(salario, porcentage_impuesto):
    calcular = (salario / 100) * porcentage_impuesto
    return calcular

print(total_impuesto(10000, 16.0))