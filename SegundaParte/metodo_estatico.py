#! /usr/bin/python
# -*- coding: utf-8 -*-
'''Script que ejemplifica el uso de un método estático.'''


class Perico():
    poblacion = 0

    def __init__(self, nombre):
        """Método que se ejecuta al instanciar un objeto."""
        self.nombre = nombre.capitalize()
        print "Salí del cascarón. Mi nombre es", self.nombre + "."
        Perico.poblacion += 1

    def habla(self):
        """Método normal."""
        print self.nombre.capitalize(), "quiere una galleta."

    def __del__(self):
        """Método que se ejecuta al descartar al objeto."""
        print "¡Ack!", self.nombre, "ha muerto."
        Perico.poblacion -= 1

    @staticmethod
    def modifica_poblacion(operador='+', numero=0):
        Perico.poblacion = eval(str(Perico.poblacion) + operador + str(numero))
        if Perico.poblacion < 0:
            Perico.poblacion = 0
        print "Ahora hay, %d pericos." % Perico.poblacion
