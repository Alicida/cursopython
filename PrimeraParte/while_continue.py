#! /usr/bin/python
# -*- coding: utf-8 -*-

''' Este programa se repetirá 3 veces y desplegará el número de intentos en los
    que se ingresó la palabra "despedida".'''

entrada = ""
suma = 0
fallido = 0
while suma < 3:
    suma += 1
    print "Intento %d." % suma
    entrada = raw_input("Clave:")
    print
    if entrada == "despedida":
        continue
    fallido += 1
print "Tuviste %d intentos fallidos." % fallido
