# ALGORITMOS DE ORDENAMIENTO

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
    return str(A)

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
    return str(A)

# Quicksort
def pivote(A):
    return A[0]   # elección arbitraria
def quicksort(A):
    pivote_elegido = pivote(A)
    menores = [x for x in A if x < pivote_elegido]
    mayores = [x for x in A if x > pivote_elegido]

    men_ord = quicksort(menores)
    may_ord = quicksort(mayores)

    return men_ord + [pivote] + may_ord


lista = [5,3,1,7]
print(ordenar_por_seleccion(lista))
print(ordenar_por_insercion(lista))
print(quicksort(lista))
