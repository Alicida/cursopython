#! /usr/bin/python
# -*- coding: utf-8 -*-

''' Este programa se repetirá 3 veces o hasta que se ingrese
    la palabra "despedida" y desplegará el número de intentos
    hasta que cualquiera de los eventos ocurra.'''

entrada = ""
suma = 0
while ((suma < 3) and (entrada != "despedida")):
    entrada = raw_input("Clave:")
    suma += 1
    print "Intento %d. \n " % suma
print "Utilizaste %d intentos." % suma
