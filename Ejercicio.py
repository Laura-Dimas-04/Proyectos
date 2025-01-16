fuscia = "\033[35m" 
blanco = "\033[97m" 


#Codigo 6.15
print(fuscia+"Este es el codigo 6.15")
def numero_mayor( a, b, c):
    if a > b:
        x = a
    else:
        x = b
    
    if c > x:
        x = c
    return x

try:
    a, b, c = map(int, input(blanco+"Ingresa 3 numeros enteros separados por espacios: ").split())
except ValueError:
    print(blanco+"Querido usuario nada mas se pueden ingresar 3 numeros por favor vuelva a iniciar.")

respuesta = numero_mayor(a, b, c)
print(blanco+"EL numero mayor entero es: ", (respuesta))


# Codigo 6.16
print(fuscia+"Este es el codigo 6.16")
class Empty(Exception):
    pass

class ArrayStack:
    #
    def __init__ (self, maxlen = None):
        self._data = [ ]
        #
        self._maxlen = maxlen
    
    def __len__ (self):
        return len(self._data)
    
    def is_empty(self):
        return len(self._data) == 0
    
    def push(self, e):
        self._data.append(e)
    
    def top(self):
        if self.is_empty( ):
            raise Empty('Stack is empty')
        return self._data[-1] 
    
    def pop(self):
        if self.is_empty( ):
            raise Empty('Stack is empty')
        return self._data.pop( )

print(blanco+"En este codigo se modifica la implementación de ArrayStack")
stack = ArrayStack(maxlen=2)
stack.push(1)
stack.push(2)
print(stack.pop())  
print(stack.pop())  
stack.push(3)

# Codigo 6.17
class Empty(Exception):
    pass
class Full(Exception):
    pass

class ArrayStack:

    def __init__(self, maxlen=None):
        self._maxlen = maxlen
        self._data = [None] * maxlen if maxlen is not None else []  
        self._size = 0  

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, e):
        if self._maxlen is not None and self._size == self._maxlen:
            raise Full("La pila está llena")
        self._data[self._size] = e  
        self._size += 1  

    def top(self):
        if self.is_empty():
            raise Empty("La pila está vacía")
        return self._data[self._size - 1] 

    def pop(self):
        if self.is_empty():
            raise Empty("La pila está vacía")
        self._size -= 1  
        return self._data[self._size]  

def interact_with_stack():
    max_capacidad = int(input(fuscia+"Ingrese la capacidad máxima de la pila: "))  
    pila = ArrayStack(maxlen=max_capacidad) 

    while True:
        print(blanco+"Qué opción desea realizar")
        print(blanco+"""
            1. Push (agregar un elemento a la parte superior de la pila)
            2. Pop (eliminar y devolver el elemento superior de la pila)
            3. Top (Mostrar el elemento superior de la pila sin eliminarlo)
            4. Verificar si la pila está vacía
            5. Salir
            """)
        opcion = input(blanco+"Ingrese el número de la opción deseada: ")

        if opcion == "1":
            if len(pila) < max_capacidad:
                elemento = input(blanco+"Ingrese el elemento que desea agregar: ")
                pila.push(elemento)
                print(blanco+"Se ha agregado {elemento} a la pila.")
            else:
                print(blanco+"La pila está llena. No se pueden agregar más elementos.")
        elif opcion == "2":
            try:
                elemento = pila.pop()
                print(blanco+"Se ha eliminado {elemento} de la pila.")
            except Empty as e:
                print("Error:", e)
        elif opcion == "3":
            try:
                elemento = pila.top()
                print(blanco+"El elemento en la parte superior de la pila es", {elemento})
            except Empty as e:
                print("Error:", e)
        elif opcion == "4":
            if pila.is_empty():
                print(blanco+"La pila está vacía.")
            else:
                print(blanco+"La pila no está vacía.")
        elif opcion == "5":
            print(blanco+"Saliendo del programa.")
            break
        else:
            print(blanco+"Opción no válida. Por favor, ingrese un número válido.")
interact_with_stack()

#Codigo 6.18
class ArrayStack:

    def __init__(self):
        self._data = []  

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, elemento):
        self._data.append(elemento)

    def top(self):
        if self.is_empty():
            raise Exception("Pila vacía")
        return self._data[-1]

    def pop(self):
        if self.is_empty():
            raise Exception("Pila vacía")
        return self._data.pop()


def transferir(pila_origen, pila_destino):
    while not pila_origen.is_empty():
        pila_destino.push(pila_origen.pop())


def invertir_pila(pila):
    pila_aux1 = ArrayStack()  # Pila auxiliar 1
    pila_aux2 = ArrayStack()  # Pila auxiliar 2
    transferir(pila, pila_aux1)
    transferir(pila_aux1, pila_aux2)
    transferir(pila_aux2, pila)

if __name__ == "__main__":
    pila_original = ArrayStack()
    for numero in range(1, 10):
        pila_original.push(numero)
    print(f"\nContenido original de la pila: {pila_original._data}")
    invertir_pila(pila_original)
    print(f"\nContenido invertido de la pila: {pila_original._data}")


# Codigo 6.20
print(fuscia+"Este es el codigo 6.20")
def enumerate_permutations(n):
    stack = [[]]
    numbers = list(range(1, n+1))

    while stack:
        current_permutation = stack.pop()
        if len(current_permutation) == n:
            print(current_permutation)
        else:
            for i in range(n):
                if numbers[i] not in current_permutation:
                    new_permutation = current_permutation + [numbers[i]]
                    stack.append(new_permutation)

try:
    print(blanco+"En este codigo se le pide al usuario que ingrese un numero y el programa generara las permutaciones.")
    n = int(input(blanco+"Ingrese el número máximo para generar las permutaciones: "))
    enumerate_permutations(n)
except:
    print(blanco+"Querido usuario solo ingrese numeros por favor.")


#Codigo 6.21
print(fuscia+"Este es el codigo 6.21")
from collections import deque

def generate_subsets(T):
    subsets = deque([[]])
    queue = deque()
    queue.append(subsets)

    while queue:
        current_subsets = queue.popleft()
        for subset in current_subsets:
            print(subset)
            for element in T:
                if element not in subset:
                    new_subset = subset + [element]
                    queue.append(deque([new_subset]))
# Ejemplo de uso
print(blanco+"En este codigo se muestra las maximas permutaciones que ingresas en el mismo codigo.")
T = [1, 2, 3,]
generate_subsets(T)


