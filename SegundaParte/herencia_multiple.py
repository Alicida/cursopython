#! /usr/bin/python
# -*- coding: utf-8 -*-


class Animal(object):

    def __init__(self, nombre):
        print "El animal %s acaba de nacer" % nombre
        self.nombre = nombre

    def reproduccion(self):
        pass


class Mamifero(Animal):

    def produce_leche(self):
        print "Aquí hay un poco de leche."

    def reproduccion(self, tiempo):
        self.tiempo_gestacion = tiempo
        print "Despueś de %d meses nacen las crías." % self.tiempo_gestacion


class Reptil(Animal):

    def produce_veneno(self, venenoso):
        self.veneno = venenoso
        if venenoso:
            print "Soy venenoso."

    def reproduccion(self):

        print "Aquí hay un huevo."


class Ornitorrinco(Reptil, Mamifero):
    def __init__(self, nombre):
        super(Ornitorrinco, self).__init__(nombre)
        print "¡qué demonios!"

perry = Ornitorrinco("Agente P")
perry.reproduccion()
perry.produce_veneno(True)
perry.produce_leche()