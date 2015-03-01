#! /usr/bin/python
# -*-coding: utf-8 -*-
import datos
import valida


def alta():
    """Realiza las altas."""
    alumno_nuevo = {}
    for identificador in datos.orden:
        valida_tipo = False
        valida_casos = False
        excepcion = False
        while not (valida_tipo and valida_casos and excepcion):
            excepcion = True
            valida_tipo = True
            valida_casos = True
            mensaje = "Ingrese " + identificador.lower() + ": "
            valor = raw_input(mensaje)
            if datos.campos[identificador] != str:
                try:
                    valor = eval(valor)
                    if datos.campos[identificador] == float:
                        valor = float(valor)
                except:
                    excepcion = False
                    continue
            valida_tipo = valida.es_el_tipo(valor, datos.campos[identificador])
            if not valida_tipo:
                continue
            valida_casos = valida.reglas(valor, identificador)
        alumno_nuevo[identificador] = valor
    return alumno_nuevo
