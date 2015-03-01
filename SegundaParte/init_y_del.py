#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Script que ejemplifica el uso de los métodos __init__() y __del__()"""


class Perico():

    def __init__(self, nombre):
        """Método que se ejecuta al instanciar un objeto."""
        self.nombre = nombre.capitalize()
        print "Salí del cascarón. Mi nombre es", self.nombre + "."

    def habla(self):
        """Método normal."""
        print self.nombre.capitalize(), "quiere una galleta."

    def __del__(self):
        """Método que se ejecuta al descartar al objeto."""
        print "¡Ack!", self.nombre, "ha muerto."

poli = Perico("poli")
juancho = Perico("Juancho")
choforo = Perico("Choforito")
raw_input("\nPulse <INTRO> para que hable Poli.")
poli.habla()
raw_input("\nPulse <INTRO> para que se resfríe Juancho.")
#El objeto juancho es desechado durante la ejecución del script
del juancho
raw_input("\nPulse <INTRO> para que termine el programa.")
'''Al terminar de ejecutarse el script, todos los objetos son desechados.
   Cuando el script es importado, los objetos existiran hasta que sean
   desechados o hasta que el entorno interactivo se cierre.'''
