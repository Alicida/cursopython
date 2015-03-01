#! /usr/bin/python
# -*- coding: utf-8 -*-

""" Ejemplo de control de excepciones para diversos errores.
    El programa pedirá un número hasta que no se generen errores
    y desplegará el cuadrado de dicho número.
    En caso de ocurrir una excepción se despelgará el mensaje de error."""

ocurre_error = True
while ocurre_error:
    try:
        numero = input("Ingrese un número: ")
        numero = float(numero)
        print "La raíz cuadrada de %f es %f" % (numero, numero ** 0.5)
    except (NameError, ValueError, TypeError) as excepcion:
        print "Mensaje de error:", excepcion
    except:
        print "¡No sé qué pasó!"
    else:
        print "No hubo errores."
        ocurre_error = False
    finally:
        if ocurre_error:
            print "Lástima."
        else:
            print "¡YAY!"
print "Buen día."
