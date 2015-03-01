#! /usr/bin/python
# -*- coding: utf-8 -*-

import math


class Forma(object):

    def __init__(self):
        pass

    def superficie(self):
        pass

    def perimetro(self):
        pass


class Circulo(Forma):

    def __init__(self, radio=1):
        self.radio = radio

    def superficie(self):
        return math.pi * self.radio ** 2

    def perimetro(self):
        return math.pi * 2 * self.radio


class Rectangulo(Forma):

    def __init__(self, base=1, altura=2):
        self.base = base
        self.altura = altura

    def superficie(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

FormaRectangular = Rectangulo()
FormaCircular = Circulo(45)
print "La superficie del rectángulo es", FormaRectangular.superficie()
print "La superficie del círculo es", FormaCircular.superficie()
