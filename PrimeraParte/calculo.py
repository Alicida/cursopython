#! /usr/bin/python
# -*-coding: utf-8 -*-
"""Script que ejemplifica las funciones con valores de retorno. Hace el cáclulo
de dos elementos en función de un operador y regresa el resultado."""


def calcula(elmento1=1, operador="+", elemento2=1):
    operacion = eval(str(elmento1) + operador + str(elemento2))
    return operacion

resultado = calcula(12, "/", 3.5)
print "El resultado del cálculo es de:", resultado
