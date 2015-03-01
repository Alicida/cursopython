#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Este es un programa que contiene una función llamada area
    para un circulo y el valor de pi"""


def area(radio):
    global pi
    pi = 3.1415926
    print "El área del círculo de radio %f es de %f" % (radio, pi * radio ** 2)

pi = "pi"
print "Valor de pi:", pi
area(2)
print "Valor de pi:", pi