#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Este script crea una lista llamada animales_domesticos a partir de la
comparacion entre la lista animales y la lista animales_salvajes"""

animales = ["perro", "gato", "jirafa", "cocodrilo", "leopardo", "chinchilla",
    "elefante"]
animales_salvajes = ["jirafa", "cocodrilo", "leopardo", "elefante"]
animales_domesticos = []
for item in animales:
    if item not in animales_salvajes:
        animales_domesticos.append(item)
print animales_domesticos
