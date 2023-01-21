# ALGORITMOS DE ORDENAMIENTO

def ordenar_por_seleccion(A):
    long = len(A)
    minimo = None
    posicion = None
    for item1 in range(long-1):
        minimo = A[item1]
        posicion = item1
        for item2 in range(item1, long):
            if A[item2] < minimo:
                minimo = A[item2]
                posicion = item2
        A[posicion], A[item1] = A[item1], A[posicion]
    return str(A)

lista = [5,8,1,3]
print(ordenar_por_seleccion(lista))