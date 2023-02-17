# DISEÑO DE ALGORITMOS
# Algoritmo de fuerza bruta y "divide y venceras"

from math import sqrt
# Dado un número entero compuesto, que es producto de dos números primos,
# hacer un algoritmo de fuerza bruta que encuentre su factorización.
# Analice la cantidad operaciones que este algoritmo requiere.

def es_solucion(nro, ejemplo):
    return nro % ejemplo == 0

def siguiente(nro, i=1):
    if i + 1 < round(sqrt(nro)):  # verifica si el positivo, mayor a dos?
        return i + 1
    return None  # resultado: ¿no tiene factorizacion?

def verificador(nro):
    intento_actual = siguiente(nro)

    while intento_actual and not es_solucion(nro, intento_actual):
        intento_actual = siguiente(nro, intento_actual)

    if intento_actual is not None:
        return (intento_actual, nro // intento_actual)

    return None

