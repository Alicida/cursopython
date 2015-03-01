#! /usr/bin/python
# -*- coding: utf-8 -*-
"""script valida"""
import datos


def es_el_tipo(dato, tipo):
    """Función de revisión de tipos"""
    if tipo not in datos.campos.values():
        return False
    elif type(dato) == tipo:
        return True
    else:
        return False


def reglas(dato, identificador):
    if identificador == "Carrera" and dato not in datos.carreras:
        return False
    elif identificador == "Semestre" and dato < 1:
        return False
    elif identificador == "Promedio" and (dato < 0 or dato > 10):
        return False
    elif (identificador in ("Nombre", "Primer Apellido") and (dato == "")):
        return False
    elif identificador == "Segundo Apellido" and dato == "":
        en_blanco = True
        while en_blanco:
            mensaje = "No ha ingresado el " + identificador.lower() + \
            ". ¿Es correcto? S/N: "
            confirma = raw_input(mensaje)
            if confirma.upper() in ("S", "N"):
                en_blanco = False
        if confirma.upper() == "N":
            return False
        else:
            return True
    else:
        return True
