#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Script que ejemplifica el modo en el que los objetos interactúan con los
distintos ámbitos."""

numero = 6


class ClaseconMetodo(object):
    """Clase que despliega un saludo varias veces en función
    de un nombre global."""

    dato = "Buen día "

    def saludo(self, nombre):
        """Método que hace uso de nombres globales, atributos,
        argumentos y nombres locales."""
        mensaje = self.dato + nombre + ".\n"
        print mensaje * numero

objeto = ClaseconMetodo()
objeto.saludo("Juan")
