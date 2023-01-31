# TABLA HASH

class NodoHash:
    def __init__(self, key=None, element=None, next=None):
        self.key = key
        self.element = element
        self.next = next
    def __str__(self):
        return f"{self.key}, {self.element}"


class HashTable:
    def __init__(self, capacity, hashfunc):
        self.capacity = capacity
        self.hash = hashfunc
        self.T = [None] * self.capacity
    def insert(self, key, element):
        pass
    def search(self, key):
        pass
    def delete(self, key):
        pass


                    # ACTIVIDADES

# **Ejercicio 1**: Implemente una clase que contenga internamente una tabla hash que inicie vacía, o sea,
# una lista del tamaño especificado y repleta del valor None.
# *Ayuda: puede usar un for, una lista por comprensión o multiplicar una lista unitaria*.

class Hash_Table:
    def __init__(self, capacity, func):
        self.cap = capacity
        self.hash = func
        self.table = [None] * self.cap

# **Ejercicio 2**: Se quiere rellenar el stock de un supermercado.
# Se sabe que los códigos de los productos van del 000 al 999.
# Se ingresa alguna cantidad arbitraria de códigos (no necesariamente todos) junto con la cantidad que hay en stock.
# Herede una clase de hashing directo y utilícela para resolver.

class Stock(Hash_Table):
    def hash_func(self, cod):
        if len(cod) == 3:
            return int(cod)
    def insert(self, codigo, cant):
        hash = self.hash_func(codigo)
        self.table[hash] = cant


# **Ejercicio 3**: Se quiere mejorar la solución anterior.
# Ahora nos dicen que si bien los códigos van del 000 al 999, nunca se ingresarán más de 50.
# Resuelva usando otra clase que implemente direccionamiento abierto con sondeo lineal,
# achicando la memoria utilizada.
# *Ayuda: utilice una clase Cell auxiliar con el código y el stock.
# No necesariamente un código termina en el índice de su hash.
# Con el sondeo lineal buscamos dónde fue realmente a parar el código buscado*


# **Ejercicio 4**: Escriba una función de hash que implemente el método de Horner con coeficiente 37.
# *Ayuda: busque la función ord*

def funchash(coeficientes):   # REVISAR
    valor = 37
    resultado = 0
    for i in range(0, len(coeficientes)):
        resultado = resultado * valor + ord(coeficientes[i])
    return resultado


# **Ejercicio 5**: Utilizando el resultado numérico de Horner,
# convierta iterativamente trozos del número a un caracter para producir un string.
# Básese en el siguiente extracto de código
# repetir esto hasta que el numero sea 0, acumular los caracteres
# caracter = chr(numero % 64 + 64)
# numero = numero // 64

a = {}
a["bla"] = 16
print(a)