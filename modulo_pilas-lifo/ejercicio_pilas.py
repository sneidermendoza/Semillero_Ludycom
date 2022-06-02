"""
Se creo una clase pila(Lifo) 
"""
class Stack:
    def __init__(self):
        self.elementos = []

    def push(self,item): 
        self.elementos.append(item)
        
    def pop(self):
        a = self.elementos.pop()
        return f"se saco este  => ({a}) elemento"
    
    def peek(self):
        return self.elementos[-1]
    
    def size(self):
        return len(self.elementos)
    
    def print(self):
        return self.elementos

a = Stack()
a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(10)
print(a.peek())
print(a.size())
print(a.print())
print(a.pop())
print(a.print())