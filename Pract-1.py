# -*- coding: utf-8 -*-

# **Ejercicio 1**: Definir la interfaz de un tipo abstracto de datos para representar una celda, 
# capaz de contener un único valor a la vez. Usar lenguaje natural.
# [...]

# **Ejercicio 2**: Basándose en la interfaz hecha en el ejercicio anterior, implementar en Python una clase Celda 
# # que respete el comportamiento descripto. 
# *Ayuda: para construir un conjunto pueden pasarle una lista o usar la sintaxis *args 
# y que reciba una cantidad arbitraria de argumentos.*

class Celda:
    def __init__(self, *args):
        self.items = args[0]
    def __str__(self):
        return str(f"{self.items}")
"""   
prueba = Celda(2,3)
print(prueba)
"""

# **Ejercicio 3**: Definir la interfaz de un Conjunto, los conjuntos son los típicos en matemática, 
# donde se definen con elementos preestablecidos, nunca cambian, y podemos preguntarnos si un elemento pertenece o no a un conjunto.
#[...]

# **Ejercicio 4**: Basándose en la interfaz hecha en el ejercicio anterior, implementar en Python una clase Conjunto 
# que respete el comportamiento descrito. Escribir tests que prueben el correcto funcionamiento de dicha interfaz.

class Conjunto:
    def __init__(self):
        self.items = (1,2,3)
    def __str__(self):
        return str(self.items)
    def exits(self, other):
        return other in self.items
"""  
prueba1 = Conjunto()
print(prueba1.exits(4))
"""

# **Ejercicio 5**: Hacer otra implementación de Conjunto, llamada ConjuntoNativo, 
# que internamente almacene elementos utilizando *set*. 
# Para ello investigue el funcionamiento de dicha estructura en Python.

class ConjuntoNativo:
    def __init__(self, *args):
        self.items = set(args)
    def __str__(self):
        return str(self.items)
"""
prueba2 = ConjuntoNativo(1,2,3,4)
print(prueba2)
"""

# **Ejercicio 6**: Rediseñe la implementación de Celda para que siga conteniendo un único elemento por vez, 
# pero se adhiera a la interfaz de Conjunto, o sea que acepte múltiples elementos en su constructor 
# y que podamos preguntar por sus elementos. Llámela CeldaConjunto.

class CeldaConjunto:
    def __init__(self, *args):
        self.items = args[0]
    def __str__(self):
        return str(f"{self.items}")
    def exits(self, other):
        return other is self.items
"""
prueba3 = CeldaConjunto(2,3)
print(prueba3.exits(4))
"""

# **Ejercicio 7**: Utilizando la clase Nodo presentada a continuación

class Nodo:
    def __init__(self, valor, siguiente = None):
        self.valor = valor
        self.siguiente = siguiente
    def __str__(self):
        return f"{self.valor}, {self.siguiente}"


# Implemente y verifique el siguiente TAD Lista Enlazada utilizando composición, 
# una clase ListaEnlazada que contenga a Nodo.

class ListaEnlazada:
    def __init__(self):
        self.items = []
        
    def agregar_principio(self, nodo):
        self.items.insert(0,nodo)
        
    def agregar_final(self, nodo):
        self.items.append(nodo)
        
    def pertenece(self,other):
        return other in self.items
    
    def __str__(self):
        resultado = "Elementos de la lista enlazada: "
        for i in self.items:
            resultado += "\n * {}".format(i)
        return resultado
        
    def quitar_principio(self):
        self.items.pop(0)
    def quitar_final(self):
        self.items.pop()
    def concatenar(self, lista):
        self.items += lista.items
"""    
nodo = Nodo(1,2)
nodo1 = Nodo(3,4)
lista = ListaEnlazada()
lista.agregar_final(nodo)
lista.agregar_final(nodo1)

nodo2 = Nodo(5,6)
nodo3 = Nodo(7,8)
lista1 = ListaEnlazada()
lista.agregar_final(nodo2)
lista.agregar_final(nodo3)

lista.concatenar(lista1)
print(lista)
"""

# **Ejercicio 8**: Modifique el ejercicio anterior para que pertenece e imprimir sean métodos recursivos en Nodo 
# y la clase ListaEnlazada simplemente llame a estos.

class Nodo:
    def __init__(self, valor, siguiente = None):
        self.valor = valor
        self.siguiente = siguiente
    def imprimir(self):
        return f"{self.valor}, {self.siguiente}"
    
    def pertenece(self,other):
        return (other in self.valor or other in self.siguiente)
    

class ListaEnlazada(Nodo):     #REVER
    def __init__(self):
        self.items = []
        
    def agregar_principio(self, nodo):
        self.items.insert(0,nodo)
    def agregar_final(self, nodo):
        self.items.append(nodo)
        
    def quitar_principio(self):
        self.items.pop(0)
    def quitar_final(self):
        self.items.pop()
    
    def concatenar(self, lista):
        self.items += lista.items

# **Ejercicio 9**: Implemente una clase ListaNativa que respete el TAD anterior, 
# y que internamente utilice listas nativas de Python.

class ListaNativa(ListaEnlazada):     #REVER
    def __init__(self,lista):
        self.items = []
        for i in lista:
            self.items.append(i)

#                                       EJERC. STACKS

# **Ejercicio 10**: Basándose en el TAD de pila, implementar una clase Stack con listas de Python

class Stack:
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def push(self,item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []

# **Ejercicio 11**: Dado un Stack, volcar su contenido en otro Stack, verificar que al vaciar el contenido de este, 
# los elementos salen en el mismo orden en que ingresaron al primero. 
# Utilizar solamente los métodos del TAD pila para resolver.
"""
pila1 = Stack()
pila1.push(1)
pila1.push(2)
pila2 = Stack()

for i in pila1.items:
    pila2.push(i)
    
print(pila2)
"""

# **Ejercicio 12**: Dado un Stack de números, reordenarlos para que estén abajo los impares y arriba los pares, 
# pero que entre números del mismo tipo preserven el orden. 
# *Ayuda: utilizar dos Stacks auxiliares de números pares e impares respectivamente*.
"""
Ejemplo:

4      4
3  =>  2
2      3
1      1


nros = Stack()
nros.push(2)
nros.push(4)
nros.push(1)
nros.push(3) 

pares = Stack()
impares =  Stack()

for i in nros.items:
    if i%2==0:
        pares.push(i)
    else:
        impares.push(i)

print(pares)
print(impares)
"""

#                                       EJERC. QUEUES

# **Ejercicio 15**: Basándose en el TAD de cola, implementar una clase Queue con listas de Python.

class Queue:
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def insert(self, nodo):
        self.items.append(nodo)
    def remove(self):
        self.items.pop(0)
    def isEmpty(self):
        return self.items == []

# **Ejercicio 16**: Implementar FastQueue, una cola que internamente utiliza dos stacks de la siguiente manera:
# * Inserta por uno de los stacks
# * Remueve por el otro stack

class FastQueue:
    def __init__(self, stack1, stack2=None):
        self.stack1 = stack1
        self.stack2 = stack2

    def isEmpty(self):
        return self.stack1 == None

    def insert(self, stack):
        nuevo = Nodo(stack)
        if self.stack1 is None:
            self.stack1 = nuevo
            self.stack2 = self.stack1
        else:
            self.stack2.siguiente = nuevo
            self.stack2 = nuevo

    def remove(self, stack):
        data = self.stack1.valor
        self.stack1 = self.stack1.siguiente
        if self.stack1 is None:
            self.stack2 = None
        return data
    
# **Ejercicio 17**: Implemente una PriorityQueue, una cola que, si bien tiene la misma interfaz que las colas normales,
# no se comporta de la misma manera. En este caso, estarán primeros los elementos con *mayor prioridad*,
# # la mayor prioridad puede ser lo que sea, pero con números sería típicamente los números más pequeños o más grandes.
# Ejemplo: Metemos 5, 2, 6, 1. Sacamos 1, 2, 5, 6

class PriorityQueue(Queue):
    def remove(self):
        mayor = 0
        for i in range(1, len(self.items)):
            if self.items[i] > self.items[mayor]:
                mayor = i   # Guarda index
        item = self.items[mayor]   # Guarda valor
        self.items[mayor:mayor+1] = []   # Borra valor
        return item

# **Ejercicio 18**: Se tiene una cola del supermercado.
# Cada cliente tiene un carrito con los productos apilados, por lo que al ponerlos en la cinta salen el orden inverso
# en el que fueron puestos en el mismo.
# Dada una cola de carritos con productos, modele el problema con las estructuras vistas hasta ahora y
# escriba una clase Cinta que contenga una cola de carritos y tenga un método *historial* que
# muestre todos los productos que la lectora vería en el orden descrito.

class Cinta:                                   #REVER
    def __init__(self, carritos):
        self.carritos = carritos
    def historial(self):
        productos = []
        while not self.carritos.isEmpty():  # Queue
            carrito = self.carritos.remove()
            while not carrito.isEmpty():  # Stack
                producto = carrito.pop()
                productos.append(str(producto))
        return productos

class Producto:
    def __init__(self, nombre):
        self.nombre = nombre

    def __str__(self):
        return str(self.nombre)

    def carrito(*nombres):
        carrito = Stack()

        for nombre in nombres:
            carrito.push(nombre)

        return carrito

#                                     EJERC. BINARY TREE

# Diseño de clase Tree:
# Implemente y verifique los siguientes métodos.
# * **nodos**: devuelve la cantidad de nodos del árbol
# * **menor_mayor**: devuelve en una tupla el menor y el mayor elemento del árbol
# * **buscar**: busca si un elemento está o no en el árbol
# * **altura**: calcula la altura del árbol, la distancia desde la raíz hasta la hoja más lejana

class Tree:
    def __init__(self, label, left=None, right=None):
        self.label = label
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.label)

    def printPreOrder(self):               #REVISAR
        if self.label is None:
            return
        print(self.label)
        self.left.printPreOrder()
        self.right.printPreOrder()

    def printInOrder(self):               #REVISAR
        if self is None:
            return
        self.left.printPreOrder()
        print(self.label)
        self.right.printPreOrder()

    def printPostOrder(self):               #REVISAR
        if self is None:
            return
        self.left.printPreOrder()
        self.right.printPreOrder()
        print(self.label)

    def cant_nodos(self):
        cant = 1
        cant += self.left.cant_nodos() if self.left is not None else 0
        cant += self.right.cant_nodos() if self.right is not None else 0
        return cant

    def menor_mayor(self):
        minimo = maximo = self.label

        if self.left is not None:
            (lminimo, lmaximo) = self.left.menor_mayor()
            minimo = min(minimo, lminimo)
            maximo = max(maximo, lmaximo)

        if self.right is not None:
            (rminimo, rmaximo) = self.right.menor_mayor()
            minimo = min(minimo, rminimo)
            maximo = max(maximo, rmaximo)

        return (minimo, maximo)

    def altura(self):
        altural = 0 if self.left is None else self.left.altura()
        alturar = 0 if self.right is None else self.right.altura()
        return 1 + max(altural, alturar)

def insertTree(data, tree):
    if data == None:
        return Tree(data)
    else:
        if data < tree.label:
            return Tree(tree.label, insertTree(data,tree.left), tree.right)
        elif data > tree.label:
            return Tree(tree.label, tree.left, insertTree(data, tree.right))
        else:
            return tree

def createTree(lista):
    arbol = None
    while lista != []:
        item = lista.pop()
        arbol = insertTree(item, arbol)
    return arbol

def buscar(data, tree):
    if tree is None:
        return f"{data} no está en este árbol"
    else:
        if data < tree.label:
            return buscar(data, tree.left)
        elif data > tree.label:
            return buscar(data, tree.right)
        else:
            return f"{data} sí está en este árbol"

rama1 = Tree(2)
rama2 = Tree(3)
rama = Tree(1, rama1, rama2)
print(rama.printPreOrder())

