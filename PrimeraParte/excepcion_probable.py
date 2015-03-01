#! /usr/bin/python
# -*- coding: utf-8 -*-

""" Ejemplo de control de excepciones.
    Este código es muy fácil de descarrilar."""

numero = input("Ingrese un número: ")
numero = float(numero)
print "La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5)
print "Buen día."