#! /usr/bin/python
# -*-coding: utf-8 -*-

"""Este script genera una excepción cuando la palabra clave coincide con el
valor indicado.
El programa se detendrá sólo si se escribe la palabra clave."""

itera = True
while itera:
    try:
        clave = raw_input("Dame la clave: ")
        assert(clave != "Alto")
    except AssertionError:
        print "Exacto."
        break
