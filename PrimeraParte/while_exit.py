#! /usr/bin/python
# -*- coding: utf-8 -*-

''' Este programa se repetirá 3 veces o hasta que se ingrese
    la palabra "despedida" y desplegará sólo el número de intentos
    fallidos hasta que cualquiera de los eventos ocurentradara. Al
    ingresar la palabra "termina" el programa flujo se detendrá.'''

entrada = ""
suma = 0
while suma < 3 and entrada != "despedida":
    entrada = raw_input("Clave:")
    if entrada == "despedida":
        break
    elif entrada == "termina":
        exit()
    suma = suma + 1
    print "Intento %d. \n " % suma
print "Tuviste %d intentos fallidos." % suma
