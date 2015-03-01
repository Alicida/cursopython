#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Módulo que cuenta los dígitos que se repiten en una cuenta sucesiva de
enteros iniciando desde el 1."""


def digito_en_conteo(digito, numero):
    """Función de conteo."""
    cuenta = 0  # contador de la veces que se repite el dígito
    for conteo in range(1, int(numero) + 1):
        for letra in str(conteo):
            if letra == str(digito):
                cuenta = cuenta + 1
    return cuenta


def programa():
    """Esta función se ejecutará cuando se importe el módulo
    en la interfaz interactiva"""
    print "Este es un módulo que cuenta los dígitos."
    tope = raw_input("¿Hasta qué número quiere contar? ")
    digito = raw_input("¿Qué dígito quiere contar? ")
    resultado = digito_en_conteo(digito, tope)
    print "El dígito '%s' se repite %d veces en un conteo del 1 al %s."  \
    % (digito, resultado, tope)
    print "El valor de __name__ es:", __name__

if __name__ == "__main__":  # No se ejecuta si se importa como módulo
    programa()
