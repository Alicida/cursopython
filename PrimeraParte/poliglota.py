#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Script que ejemplifica el uso de diccionarios y el operador in.
Se desplegará un texto predeterminado en el idioma seleccionado."""

es = {"nombre": "¿Cuál es su nombre? ", "saludo": "Buen día,"}
en = {"nombre": "What is your name? ", "saludo": "Hello,"}
diccionario = {"EN": en, "ES": es}
idioma = raw_input("Seleccione idioma / Select language (ES/EN): ")
idioma = idioma.upper()
if idioma not in diccionario:
    print("Idioma no identificado. Se utilizará ES por defecto.")
    idioma = "ES"
nombre = raw_input(diccionario[idioma]["nombre"])
print diccionario[idioma]["saludo"], nombre + "."
