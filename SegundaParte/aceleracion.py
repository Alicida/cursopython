#! /usr/bin/python
# -*- coding: utf-8 -*-
"""Módulo que calcula el desplazamientos de los cuerpos en caída libre
utilizando diversas unidades de medida."""


class CaidaLibre(object):
    """Realiza cálculos relativos a la caída libre de los objetos dentro del
    campo gravitacional terrestre. """
    gravedad = 9.80665
    longitudes = {"pies": 3.28084, "pulgadas": 39.3701, "yardas": 1.09361,
                "metros": 1.0, "millas": 0.000621371, "kilometros": 0.001}
    tiempos = {"segundos": 1, "minutos": 1. / 60, "horas": 1. / 3600}

    def __init__(self, longitud="metros", tiempo="segundos"):
        """Se definen las unidades de longitud y tiempo a utilizar."""
        if longitud in self.longitudes.keys():
            self.longitud = longitud
            print "Unidades de longitud en %s." % self.longitud
        else:
            print "No se dio una unidad válida. Se utilizarán metros."
            self.longitud = "metros"
        if tiempo in self.tiempos.keys():
            self.tiempo = tiempo
            print "Unidades de tiempo en %s." % self.tiempo
        else:
            print "No se dio una unidad válida. Se utilizarán segundos."
            self.tiempo = "segundos"

    def distancia(self, tiempo=1):
        """Calcula la distancia recorrida por el objeto suponiendo que estaba
        en reposo."""
        return self.longitudes[self.longitud] * (self.gravedad *
               (tiempo / self.tiempos[self.tiempo]) ** 2) / 2

    def velocidad(self, tiempo=1):
        """Calcula la velocidad del objeto suponiendo que estaba
        en reposo."""
        return ((self.gravedad * tiempo / self.tiempos[self.tiempo]) *
               (self.longitudes[self.longitud] / self.tiempos[self.tiempo]))

    def despliega(self, tiempo=1):
        """Despliega la información relativa a desplazamiento y velocidad
        en función del tiempo."""
        print "La distancia recorrida en %.3f %s es de %.3f %s." % (tiempo,
           self.tiempo, self.distancia(tiempo), self.longitud)
        print "La velocidad alcanzada en %.3f %s es de %.3f %s/%s.\n" % (tiempo,
           self.tiempo, self.velocidad(tiempo), self.longitud, self.tiempo)


def calculos():
    """Realiza cálculos predefinidos. Mismo tiempo y distancia
    en distintas unidades."""

    caida = CaidaLibre()
    caida.despliega(180)
    otrasunidades = CaidaLibre("kilometros", "horas")
    otrasunidades.despliega(0.05)
    otramas = CaidaLibre("millas", "minutos")
    otramas.despliega(3)
    caida.gravedad = 16
    caida.despliega(180)

if __name__ == "__main__":
    calculos()
