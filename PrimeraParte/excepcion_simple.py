#! /usr/bin/python
# -*- coding: utf-8 -*-

""" Ejemplo de control de excepciones básico.
    El programa pedirá un número y desplegará la raíz cuadrada de dicho número.
    El código dirigirá cualquier error al bloque de código anidado en except."""

ocurre_error = False
try:
    numero = input("Ingrese un número:")
    numero = float(numero)
    print "La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5)
except:
    ocurre_error = True
if ocurre_error:
    print "Lástima"
else:
    print "Buen día."
