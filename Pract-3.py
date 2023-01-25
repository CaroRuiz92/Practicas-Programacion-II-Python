# ALGORITMOS DE ORDENAMIENTO
import random


# Ordenamiento por selección

def ordenar_por_seleccion(A):
    long = len(A)
    minimo = None
    posicion = None
    for item1 in range(long-1):   # todos serán tomados como el mínimo
        minimo = A[item1]
        posicion = item1
        for item2 in range(item1, long):   # desde el item seleccionado hasta el final
            if A[item2] < minimo:
                minimo = A[item2]
                posicion = item2
        A[posicion], A[item1] = A[item1], A[posicion]
    return A

# Ordenamiento por inserción

def ordenar_por_insercion(A):
    long = len(A)
    for pos in range(1, long):
        item = A[pos]
        anterior = pos-1
        while anterior >= 0:
            if item < A[anterior]:
                A[anterior+1] = A[anterior]   # se reemplaza el valor evaluado por el anterior (adelanta)
                anterior = anterior-1
            else:
                break
        A[anterior+1] = item
    return A

# Quicksort

def pivote(A):
    return A[0]   # elección arbitraria
def quicksort(A):
    pivote_elegido = pivote(A)
    menores = [x for x in A if x < pivote_elegido]
    mayores = [x for x in A if x > pivote_elegido]

    men_ord = quicksort(menores)
    may_ord = quicksort(mayores)

    return men_ord + [pivote_elegido] + may_ord
"""
lista = [5,3,1,7]
print(ordenar_por_seleccion(lista))
print(ordenar_por_insercion(lista))
print(quicksort(lista))
"""

#                               Ejercicios

# **Ejercicio 1**: Implementar una cola de prioridad que internamente mantenga
# los elementos ordenados utilizando ordenamiento por inserción.

class PriorityQueue:
    def __init__(self):
        self.items = []
    def __str__(self):
        return str(self.items)
    def insert(self, elem):
        self.items.append(elem)
        long = len(self.items)
        for pos in range(1, long):
            item = self.items[pos]
            anterior = pos - 1
            while anterior >= 0:
                if item < self.items[anterior]:
                    self.items[anterior + 1] = self.items[anterior]
                    anterior = anterior - 1
                else:
                    break
            self.items[anterior + 1] = item
        return str(self.items)

    def remove(self):
        self.items.pop(0)
    def isEmpty(self):
        return self.items == []

"""
prueba = PriorityQueue()
prueba.insert(2)
prueba.insert(1)
prueba.insert(5)
prueba.insert(4)
print(prueba)
"""

# **Ejercicio 2**: Escribir una función que verifique eficientemente si una lista está ordenada,
# utilícela para implementar _bogosort_:
# Utilice bogosort para ordenar [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] y observe el tiempo que le toma.

# Versión 1:
def verificar_orden1(lista):   # específico para el ejemplo dado
    if len(lista) < 2:
        return "Ordenada de forma trivial"
    for num in range(len(lista)-1):
        if lista[num] == num+1:
            return "Está ordenada"
        else:
            return "No está ordenada"

# Versión 2:
def verificar_orden2(lista):   # más general para cualquier ejemplo
    if len(lista) < 2:
        return True
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False   # si no está de forma ascendente
    return True

def bogosort(lista):
    while not verificar_orden2(lista):
        random.shuffle(lista)
    return lista

"""
ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ejemplo1 = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
print(verificar_orden2(ejemplo))
print(bogosort(ejemplo1))
"""

# **Ejercicio 3**: Se les da una lista de números enteros. Determinar la cantidad de elementos únicos, o sea,
# la cantidad de elementos ignorando los repetidos.
# **Nota**: Utilice ordenamiento para resolver.
# [1, 5, 3, 3, 5, 1]
# # Salida: 3
# Resolver de forma eficiente: que sea capaz de computar la solución
# para una lista de 10000 elementos en aproximadamente un segundo.

def verificar_unicos(lista):
    items = ordenar_por_seleccion(lista)
    cont = []
    for i in items:
        if i not in cont:
            cont.append(i)
    return f"La lista tiene {len(cont)} elementos únicos"

"""
ej = [1, 5, 3, 3, 5, 1]
print(verificar_unicos(ej))
"""

# **Ejercicio 4**: Reescribir quicksort para que tenga un parámetro más: una función de comparación.
# La función de comparación será cualquiera que, dados dos elementos de la lista, devuelve:
# - -1 si el primer elemento va antes
# - 0 si son iguales
# - 1 si el segundo elemento va antes.
# Esto es así para facilitar la implementación, ya que no incluimos el pivot en nuestra recursión.

def comparacion(a, b):
    if a == b:
        return "0"
    elif a < b:
        return "-1"
    else:
        return "1"

def elegir_pivote(lista):
    return int(lista[0])

def quicksort_b(lista, compare):
    if len(lista) < 2:
        return True
    piv = elegir_pivote(lista)
    menores = [x for x in lista if comparacion(x, piv) == "-1"]
    mayores = [x for x in lista if comparacion(x, piv) == "1"]
    return [quicksort_b(menores, comparacion)] + [piv] + [quicksort_b(mayores, comparacion)]

# COMPLETAR

