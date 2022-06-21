"""Tenemos una secuencia con las marcas de tiempo de una emisión de señal. Cada marca
de tiempo es un número de segundos entre cero y cincuenta y nueve. Transcurre al
menos un segundo y como máximo un minuto entre dos marcas de tiempo consecutivas.
Queremos saber si el emisor es un metrónomo, es decir, si emite a intervalos de tiempo
constantes. Por ejemplo, la secuencia 15 40 5 es compatible con un metrónomo que
emite cada 25 segundos.
El programa tiene que documentar, codificar y usar la función:
int time_lapse(int time_1, int time_2)
que, dadas dos marcas de tiempo consecutivas de la secuencia de entrada, devuelve el
tiempo transcurrido en segundos.
Input
Una secuencia con dos o más marcas de tiempo en segundos. Cada marca de tiempo es
un número entero entre 0 y 59. El tiempo transcurrido entre dos marcas de tiempo
consecutivas es mayor o igual a un segundo y menor o igual a un minuto. Después de la
secuencia de marca de tiempo, aparece la marca -1.
Output
La salida es un número. En el caso de que la secuencia sea compatible con un
metrónomo es el número de segundos que pasan entre dos señales consecutivas. Si la
secuencia no es compatible con un metrónomo, el número en la salida es 0.
Observation
No puedes usar vectores para resolver este problema.
Public test cases
 Input
10 25 40 55 10 25 40 -1
Output
15
 Input
1 3 5 7 11 13 -1
Output
0
 Input
47 47 47 -1
Output
60
 Input
12 6 -1
Output
54"""



a = int(input("Ingrese el tiempo ->")) 
b = int(input("Ingrese el tiempo ->"))
c = int(input("Ingrese el tiempo ->"))
cierto = True



def time_lapse(time_1, time_2):
    if time_1 < time_2 : return time_2 - time_1
    else: return 60 - (time_1 -time_2)

lapso = time_lapse(a,b)

while c != -1 and cierto:
    nuevo_lapso = time_lapse(b,c)
    cierto = lapso == nuevo_lapso
    b = c
    c = int(input("Ingrese el tiempo ->"))

if cierto: print(lapso)
else: print(0)