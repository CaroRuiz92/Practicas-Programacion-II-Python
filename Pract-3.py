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

    return [men_ord] + [pivote_elegido] + [may_ord]

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

def verificar_orden(lista):
    if len(lista) < 2:
        return True
    for i in range(len(lista)-1):
        if lista[i] > lista[i+1]:
            return False
    return True

def bogosort(lista):
    while not verificar_orden(lista):
        random.shuffle(lista)
    return lista

"""
ejemplo = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ejemplo1 = [5, 6, 7, 8, 9, 10, 1, 2, 3, 4]
print(verificar_orden(ejemplo))
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

def comp(a,b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

def quicksort_b(lista):
    if len(lista) < 2:
        return True
    pivote = lista[0]
    menores = [x for x in lista if comp(x, pivote) == -1]
    mayores = [x for x in lista if comp(x, pivote) == 1]
    return [quicksort_b(menores)] + [pivote] + [quicksort_b(mayores)]   # REVER Y COMPLETAR


# **Ejercicio 5**: Se tiene la clase de tiempo mostrada a continuación, almacena horas, minutos y segundos:
#
# class Time:
#   def __init__(self, hh, mm, ss):
#     self.hh = hh
#     self.mm = mm
#     self.ss = ss
# Definir los operadores relacionales necesarios para
# poder ordenar una lista de tiempos utilizando uno de los algoritmos generalizados.

class Time:
    def __init__(self, hh, mm, ss):
        self.hh = hh
        self.mm = mm
        self.ss = ss
    def __str__(self):
        return "{}:{}:{}".format(self.__formato(self.hh), self.__formato(self.mm), self.__formato(self.ss))
    def __formato(self, num):
        if num <= 9:
            return f"0{num}"
        else:
            return f"{num}"
    def __eq__(self, other):
        return self.hh == other.hh and self.mm == other.mm and self.ss == other.ss
    def __lt__(self, other):
        if self.hh < other.hh:
            return True
        elif self.hh == other.hh and self.mm < other.mm:
            return True
        else:
            return False
    def __gt__(self, other):
        if other.hh < self.hh:
            return True
        elif self.hh == other.hh and other.mm < self.mm:
            return True
        else:
            return False

def comparar_tiempo(lista):
    tam = len(lista)
    for i in range(1, tam):
        item = lista[i]
        anterior = i-1
        while anterior >= 0:
            if item < lista[anterior]:
                lista[anterior+1] = lista[anterior]
                anterior -= 1
            else:
                break
        lista[anterior+1] = item
    return "{}".format(lista)


time1 = Time(13, 7, 59)
time2 = Time(15, 1, 32)
time3 = Time(13, 6, 59)
time4 = Time(13, 7, 50)
ej1 = [time1, time2, time3]
print(comparar_tiempo(ej1))   # REVER FORMATO DE IMPRESIÓN


