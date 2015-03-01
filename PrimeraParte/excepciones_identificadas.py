#! /usr/bin/python
# -*- coding: utf-8 -*-

""" Ejemplo de control de excepciones para diversos errores identificados.
    En caso de que ocurra un error inesperado, se desplegará una advertencia.
    El programa pedirá un número y desplegará la raíz cuadrada de dicho número.
    """

ocurre_error = False
try:
    numero = input("Ingrese un número: ")
    numero = float(numero)
    print "La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5)
except (ValueError, TypeError):
    ocurre_error = True
    print "Ocurrió un error previsto."
except NameError:
    ocurre_error = True
    print "Ocurrió un error de nombre."
except:
    ocurre_error = True
    print "¡No sé qué pasó!"
if ocurre_error:
    print "Lástima."
else:
    print "¡YAY!"
