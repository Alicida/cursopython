#! /usr/bin/python
# -*- coding: utf-8 -*-


import math
import pickle


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


with open("/home/josech/persistente.txt", "r") as persistente:
    Rectangular = pickle.load(persistente)
    print Rectangular.superficie()
    print Rectangular.base