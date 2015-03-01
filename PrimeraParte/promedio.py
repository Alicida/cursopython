#! /usr/bin/python
# -*- coding: utf-8 -*-
'''Script que ejemplifica el uso de funciones con parámetros múltiples en forma
   de tuplas.
   El programa calcula el promedio de una muestra con un número arbitrario de
   elementos'''


def promedio(nombre, *muestra):
    print "La muestra de nombre %s es:" % nombre
    print muestra
    n = len(muestra)
    print "Hay %d elementos en la muestra." % n
    media = float(sum(muestra)) / n
    print "El promedio es:", media

promedio("Serie", 1, 2, 3, 4, 5, 7)
print
promedio("Espacio muestral", 14.5, 12.7, 33.6, 54, 78, 94.12)
print
promedio(1, 1, 2, 3, 5, 8, 13, 21)
