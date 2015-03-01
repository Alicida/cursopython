#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Script que ilustra la persistencia de objetos mediante el uso
del módulo pi8kle"""

import pickle
lista = [[1, 2, 3], [4, 5, 6]]
"""Se guarda el objeto"""
with open("objeto.bin", "wb") as archivo:
    pickle.dump(lista, archivo)
"""Se recupera el objeto"""
with open("objeto.bin", "rb") as archivo:
    otra_lista = pickle.load(archivo)
print "La lista es:", lista
print id(lista)
print id(otra_lista)
if lista == otra_lista:
    print"Estas listas son idénticas."
else:
    print"Estas listas no son iguales."
