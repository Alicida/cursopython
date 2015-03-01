#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Ejemplo de nombres locales y globales en Python"""

nombre_global = 1


def funcion(nombre_local):
    """Funcion que despliega los nombres locales y globales"""
    print "Nombres locales en la funcion:\n"
    print locals()
    print "\nNombres globales:\n"
    print globals()

funcion('hola')
print "\nNombres locales en espacio de nombres principal:\n\n", locals(), "\n"
