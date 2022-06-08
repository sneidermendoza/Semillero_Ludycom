"""
Un río digital es una secuencia de números donde el número
que sigue a (n) es (n) más la
suma de sus dígitos. Por ejemplo, 12345 es seguido por 12360,
porque 12345 + 1 + 2 + 3 + 4 + 5 = 12360.

Si el primer número de un río digital es k, 
entonces llamamos a esta secuencia río k. 
Por ejemplo, el río 480 es la secuencia 480, 492, 507, 519, ...
y el río 483 es la secuencia 483, 498, 519, ...
Al igual que los ríos con agua, los ríos digitales pueden encontrarse.
Esto sucede cuando dos ríos digitales comparten algunos de sus valores.
Por ejemplo: el río 480 se encuentra con el río 483 en valor 519,
y se encuentra con el río 507 en valor 507. Sin embargo,
nunca encuentra el río 481.
Se puede demostrar que cualquier río digital se encontrará con el río 1,
el río 3 o el río 9.
Por esta razón, escriba la función
int encuentro_de_rios( int n)
que, dado un número natural n, 
devuelve el primer valor para el cual el río n se encuentra
con los ríos 1, 3 o 9.
Condición previa
Se sabe que 1 ≤ n ≤ 16384.
"""
def suma_digitos(z):
    if z < 10: return int(z)
    else: return int(z%10 + suma_digitos(z/10))


def siguiente(a):
    return a + suma_digitos(a)

def encuentro_de_rios(n):
    rio_1 = 1
    rio_3 = 3
    rio_9 = 9
    while n != rio_1 and n != rio_3 and n != rio_9:
        if n > rio_1: rio_1 = siguiente(rio_1)
        elif n > rio_3: rio_3 = siguiente(rio_3)
        elif n > rio_9: rio_9 = siguiente(rio_9)
        else: n = siguiente(n)
    return n

print(encuentro_de_rios(22))


