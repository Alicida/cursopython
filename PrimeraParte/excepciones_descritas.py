#! /usr/bin/python
# -*- coding: utf-8 -*-

""" Ejemplo de control de excepciones para diversos errores identificados.
    En caso de que ocurra un error inesperado, se desplegará una advertencia.
    La advertencia incluirá el mensaje de Python que describe el error.
    El programa pedirá un número y desplegará la raíz cuadrada de dicho número.
    """

ocurre_error = False
try:
    numero = input("Ingrese un número: ")
    numero = float(numero)
    print "La raíz cuadrada del número %f es %f" % (numero, numero ** 0.5)
except (ValueError, TypeError) as descripcion:
    ocurre_error = True
    print "Ocurrió un error previsto:", descripcion
except NameError as descripcion:
    ocurre_error = True
    print "Ocurrió un error de nombre:", descripcion
except:
    ocurre_error = True
    print "¡No sé qué pasó!"
if ocurre_error:
    print "Lástima."
else:
    print "¡YAY!"
