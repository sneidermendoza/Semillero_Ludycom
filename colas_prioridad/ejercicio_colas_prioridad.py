from queue import PriorityQueue


cliente = PriorityQueue() # Crear la cola de prioridad




cliente.put((10, "python")) # Añadir elementos a la cola de prioridad
cliente.put((8, "C#")) 
cliente.put((3, "javaScript")) 

print(cliente.qsize()) # Contar cuantos elementos tiene la cola de prioridad


while cliente:# Recorrer la cola de prioridad
   print(cliente.get()) # Sacar el menor elemento de la cola de prioridad
 

