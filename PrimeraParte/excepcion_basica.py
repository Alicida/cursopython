#! /usr/bin/python
# -*- coding: utf-8 -*-

""" Ejemplo de control de excepciones básico.
    El programa pedirá un número y desplegará la raíz cuadrada de dicho número.
    El código dirigirá cualquier error al bloque de código anidado en except.
    en este caso, no ocurrirá nada y el programa continuará hasta el final."""

try:
    numero = input("Ingrese un número:")
    numero = float(numero)
    print "La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5)
except:
    pass
print "Buen día."
