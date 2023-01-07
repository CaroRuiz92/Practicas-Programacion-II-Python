# -*- coding: utf-8 -*-
# **Ejercicio 1**: Definir una clase Carta que contenga todos los atributos necesarios para describir las cartas españolas.

class CartaEspañola:
    def __init__(self, nro, palo):
        self.nro = nro
        self.palo = palo
    def __str__(self):
        return f"{self.nro} de {self.palo}"


# **Ejercicio 2**: Instanciar objetos que representen el As de espadas, el 3 de copas y el Rey de bastos

prueba1 = CartaEspañola(1, "espadas")
prueba2 = CartaEspañola(3, "copas")
prueba3 = CartaEspañola(12, "bastos")


# **Ejercicio 3**: Definir un método que nos permita imprimir las cartas como lo haríamos naturalmente. 
# Ejemplo: 5 de Basto.

class CartaEspañola:
    def __init__(self, nro, palo):
        self.nro = nro
        self.palo = palo
    def __str__(self):
        if self.nro == 1:
            return f"As de {self.palo}"
        elif self.nro == "comodin" or self.palo == "comodin":
            return "Comodín"
        elif self.nro == 12:
            return f"Rey de {self.palo}"
        else:
            return f"{self.nro} de {self.palo}"
        
prueba = CartaEspañola(12, "bastos")
print(prueba)


# **Ejercicio 4**: Escribir un método que nos permita comparar cartas por igualdad (mismo número y palo).

class CartaEspañola:
    def __init__(self, nro, palo):
        self.nro = nro
        self.palo = palo
    def __str__(self):
        if self.nro == 1:
            return f"As de {self.palo}"
        elif self.nro == "comodin" or self.palo == "comodin":
            return "Comodín"
        elif self.nro == 12:
            return f"Rey de {self.palo}"
        else:
            return f"{self.nro} de {self.palo}"
    def __eq__(self, other):
        return self.nro == other.nro and self.palo == other.palo
  
prueba1 = CartaEspañola(8, "espadas")
prueba2 = CartaEspañola(8, "oro")
print(prueba1 == prueba2)


# **Ejercicio 5**: Escribir una clase Mazo, que construya el mazo de cartas españolas. 
# Escribir un método que devuelve cuántas cartas hay en el mazo.

class Mazo:
    def __init__(self):
        self.mazo = []
    
    def __str__(self):
        resultado = "Cartas del mazo: "
        for carta in self.mazo:
            resultado += "\n * {}".format(carta)
        return resultado
    
    def agregar_carta(self, carta: CartaEspañola):
        self.mazo.append(carta)
    
    def contar_cartas(self):
        print("El mazo cuenta con", len(self.mazo), "cartas")


mazo = Mazo()
mazo.agregar_carta(CartaEspañola(2, "bastos"))
mazo.agregar_carta(CartaEspañola(3, "oro"))
mazo.agregar_carta(CartaEspañola(4, "espadas"))

print(mazo.contar_cartas())


# **Ejercicio 6**: Escribir un método en la clase Mazo que *mezcle* el mazo. 
# Puede ser de utilidad el módulo [`random`] de la biblioteca estándar de Python.

import random
class Mazo:
    def __init__(self):
        self.mazo = []
    
    def __str__(self):
        resultado = "Cartas del mazo: "
        for carta in self.mazo:
            resultado += "\n * {}".format(carta)
        return resultado
    
    def agregar_carta(self, carta: CartaEspañola):
        self.mazo.append(carta)
    
    def contar_cartas(self):
        print("El mazo cuenta con", len(self.mazo), "cartas")
    
    def mezclar(self):
        random.shuffle(self.mazo)
        result = ""
        for carta in self.mazo:
            result += "\n * {}".format(carta)
        return result
                                                   
mazo = Mazo()
mazo.agregar_carta(CartaEspañola(2, "bastos"))
mazo.agregar_carta(CartaEspañola(3, "oro"))
mazo.agregar_carta(CartaEspañola(4, "espadas"))

print(mazo.mezclar())


# Ejercicio 7: Implementar en la clase Mazo, un método que permita sacar una carta específica del mazo, 
# y que devuelva True si la carta estaba presente o False si no lo estaba.

import random
class Mazo:
    def __init__(self):
        self.mazo = []
    
    def __str__(self):
        resultado = "Cartas del mazo: "
        for carta in self.mazo:
            resultado += "\n * {}".format(carta)
        return resultado
    
    def agregar_carta(self, carta: CartaEspañola):
        self.mazo.append(carta)
    
    def contar_cartas(self):
        print("El mazo cuenta con", len(self.mazo), "cartas")
    
    def mezclar(self):
        random.shuffle(self.mazo)
        result = ""
        for carta in self.mazo:
            result += "\n * {}".format(carta)
        return result
    
    def verificar(self, other):
        if other in self.mazo:
            return True
        else:
            return False


mazo = Mazo()
mazo.agregar_carta(CartaEspañola(2, "bastos"))
mazo.agregar_carta(CartaEspañola(3, "oro"))
mazo.agregar_carta(CartaEspañola(4, "espadas"))

print(mazo.verificar(CartaEspañola(2, "bastos")))


# **Ejercicio 8**: Implementar un método `sacar_carta` para robar una carta del mazo, es decir, 
# para sacar aquella que se encuentra primera, en la cima del mazo.

import random
class Mazo:
    def __init__(self):
        self.mazo = []
    
    def __str__(self):
        resultado = "Cartas del mazo: "
        for carta in self.mazo:
            resultado += "\n * {}".format(carta)
        return resultado
    
    def agregar_carta(self, carta: CartaEspañola):
        self.mazo.append(carta)
    
    def contar_cartas(self):
        print("El mazo cuenta con", len(self.mazo), "cartas")
    
    def mezclar(self):
        random.shuffle(self.mazo)
        result = ""
        for carta in self.mazo:
            result += "\n * {}".format(carta)
        return result
    
    def verificar(self, other):
        if other in self.mazo:
            return True
        else:
            return False
        
    def sacar_carta(self):
        return self.mazo.pop()

mazo = Mazo()
mazo.agregar_carta(CartaEspañola(2, "bastos"))
mazo.agregar_carta(CartaEspañola(3, "oro"))
mazo.agregar_carta(CartaEspañola(4, "espadas"))
print(mazo.sacar_carta())


# **Ejercicio 9**: Implementar un método que nos permita saber si quedan cartas en el mazo

import random
class Mazo:
    def __init__(self):
        self.mazo = []
    
    def __str__(self):
        resultado = "Cartas del mazo: "
        for carta in self.mazo:
            resultado += "\n * {}".format(carta)
        return resultado
    
    def agregar_carta(self, carta: CartaEspañola):
        self.mazo.append(carta)
    
    def contar_cartas(self):
        print("El mazo cuenta con", len(self.mazo), "cartas")
    
    def mezclar(self):
        random.shuffle(self.mazo)
        result = ""
        for carta in self.mazo:
            result += "\n * {}".format(carta)
        return result
    
    def verificar(self, other):
        if other in self.mazo:
            return True
        else:
            return False
        
    def sacar_carta(self):
        return self.mazo.pop()
    
    def is_empty(self):
        if self.mazo == []:
            return "Mazo vacío"

mazo = Mazo()
mazo.agregar_carta(CartaEspañola(2, "bastos"))
mazo.agregar_carta(CartaEspañola(3, "oro"))
mazo.agregar_carta(CartaEspañola(4, "espadas"))
print(mazo.sacar_carta())
print(mazo.sacar_carta())
print(mazo.sacar_carta())
print(mazo.is_empty())


# **Ejercicio 10** Escribir una clase Mano, que represente la mano de un jugador en algún juego de cartas. 
# Tener en cuenta que necesitaremos los métodos `sacar_carta` y otros ya definidos en Mazo. 
# Además, necesitaremos asociar el nombre del jugador que tiene esta mano.

class Mano(Mazo):
    def __init__(self,jugador):
        self.mano = []
        self.jugador = jugador


# **Ejercicio 11**: Necesitaremos que una mano tenga funcionalidad para agregar cartas a la mano y sacar cartas de la mano. ¿Cuántos métodos debemos definir? Definir solamente aquellos métodos necesarios.

class Mano(Mazo):
    def __init__(self,jugador):
        self.mano = []
        self.jugador = jugador
    def agregar_carta(self, carta: CartaEspañola):
        self.mano.append(carta)
    def sacar_carta(self):
        return self.mano.pop()

# **Ejercicio 12**: Agregar al mazo un método para repartir cartas. El método deberia recibir una lista de manos, 
# las cuales reciben las cartas, y la cantidad de cartas a repartir en cada mano.

import random
class Mazo:
    def __init__(self):
        self.mazo = []
    
    def __str__(self):
        resultado = "Cartas del mazo: "
        for carta in self.mazo:
            resultado += "\n * {}".format(carta)
        return resultado
    
    def agregar_carta(self, carta: CartaEspañola):
        self.mazo.append(carta)
    
    def contar_cartas(self):
        print("El mazo cuenta con", len(self.mazo), "cartas")
    
    def mezclar(self):
        random.shuffle(self.mazo)
        result = ""
        for carta in self.mazo:
            result += "\n * {}".format(carta)
        return result
    
    def verificar(self, other):
        if other in self.mazo:
            return True
        else:
            return False
        
    def sacar_carta(self):
        return self.mazo.pop()
    
    def is_empty(self):
        if self.mazo == []:
            return "Mazo vacío"
        
    def repartir(self, listamanos, cantcartas):   #REVER
        while len(self.mazo) >= (len(listamanos)*cantcartas): 
            for i in listamanos:
                carta = self.mazo.pop() 
                i.mano.append(carta)

mazo = Mazo()
mazo.agregar_carta(CartaEspañola(2, "bastos"))
mazo.agregar_carta(CartaEspañola(3, "oro"))
mazo.agregar_carta(CartaEspañola(4, "espadas"))
mazo.agregar_carta(CartaEspañola(5, "copas"))
mazo.agregar_carta(CartaEspañola(6, "oro"))
mazo.agregar_carta(CartaEspañola(7, "espadas"))
mano1 = Mano("Carolina")
mano2 = Mano("Milton")
mazo.repartir([mano1, mano2], 2)
print(mano1)
print(mano2)


# **Ejercicio 13**: Agregar funcionalidad para imprimir una mano, mostrando a quien pertenece y cuales cartas contiene.

class Mano(Mazo):
    def __init__(self,jugador):
        self.mano = []
        self.jugador = jugador
    def __str__(self):
        resultado = f"Cartas de la mano que pertenecen a {self.jugador}: "
        for carta in self.mano:
            resultado += "\n {}".format(carta)
        return resultado
    def agregar_carta(self, carta: CartaEspañola):
        self.mano.append(carta)
    def sacar_carta(self):
        return self.mano.pop()
    
mano = Mano("Carolina")
mano.agregar_carta(CartaEspañola(5, "copas"))
mano.agregar_carta(CartaEspañola(7, "oro"))
print(mano)
