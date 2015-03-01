#! /usr/bin/python
#-*- coding: utf-8 -*-
"""""Script que ejemplifica las funciones capaces de recibir múltiples
parámetros. En este caso sun funciones que convierten los parámetros en un
diccionario.
Se calculará la superficie de la figura geométrica conforme a su tipo y medidas
particulares."""


def superficie(**dato):
    if dato["tipo"] == "Rectángulo":
        superficie = float(dato["base"]) * float(dato["altura"])
    elif dato["tipo"] == "Triángulo":
        superficie = float(dato["base"]) * float(dato["altura"]) / 2
    elif dato["tipo"] == "Círculo":
        superficie = float(dato["radio"]) ** 2 * 3.14259265
    else:
        print "No puedo calcular la superficie."
    print "La superficie del %s es de %.3f" % (dato["tipo"].lower(), superficie)

superficie(base=2, altura=3, tipo="Triángulo")
superficie(tipo="Círculo", radio=3)
superficie(tipo="Triángulo", radio=4)