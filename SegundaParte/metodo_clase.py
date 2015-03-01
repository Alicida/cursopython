#! /usr/bin/python
# -*- coding: utf-8 -*-
'''Script que ejemplifica el uso de un método de clase.'''


class CaidaLibre(object):
    '''clase que realiza el cálculo de la distancia recorrida por un objeto
    al caer libremente desde un estado de reposo en un tiempo definido.'''
    gravedad = 9.81  # coeficiente en metros sobre segundos cuadrados

    @classmethod
    def cambia_a_pies(cls):
        '''Método que cambia el coeficiente gravitacional a pies sobre segundo
        al cuadrado para todas las instancias de la clase'''
        cls.gravedad = 32.174

    def calculo(self, tiempo):
        return (self.gravedad * tiempo ** 2) / 2

'''Instanciamos dos objetos de la misma clase'''
calculadora = CaidaLibre()
otra_calculadora = CaidaLibre()
tiempo = float(raw_input("Ingrese el tiempo de caída en segundos: "))
print "La distancia recorrida en metros es:,", calculadora.calculo(tiempo)
print "\nCambiamos las unidades a pies en todas las instancias."
calculadora.cambia_a_pies()
print "\nLa distancia recorrida en pies es:", calculadora.calculo(tiempo)
print "La distancia recorrida en pies es:", otra_calculadora.calculo(tiempo)
