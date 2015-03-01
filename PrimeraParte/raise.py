#! /usr/bin/python
# -*- coding:utf-8 -*-

""" Este programa levantará una excepción con un mensaje propio en caso de que
    el número ingresado sea negativo.
    El programa pedirá un número y desplegará la raíz cuadrado de dicho número.
    En caso de que ocurra un error definido, el programa desplegará el mensaje
    correspondiente."""

ocurre_error = True
while ocurre_error:
    try:
        numero = input("Ingrese un número: ")
        numero = float(numero)
        if numero < 0:
            raise ValueError("No es posible calcular la raíz de un negativo.")
    except (NameError, SyntaxError):
        print "Ocurrió una excepción identificada."
    except ValueError, mensaje:
        print mensaje
    except:
        print "¡No sé qué pasó!"
    else:
        print "No hubo errorres"
        ocurre_error = False
    finally:
        if ocurre_error:
            print "Lástima"
        else:
            print "¡YAY!"
print "La raíz cuadrada de %.2f es %.2f" % (numero, numero ** 0.5)
