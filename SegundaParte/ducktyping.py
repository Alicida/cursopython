#! /usr/bin/python
# -*- coding: utf-8 -*-
'''Script que ilustra el uso de duck typing'''


class CapitalesMundiales(object):
    capitales = {
                "México": "Distrito Federal",
                "Argentina": "Buenos Aires",
                "Uruguay": "Montevideo",
                "Brasil": "Sao Paulo",
                "Estados Unidos": "Washington, D.C."
                }

    def __init__(self, pais="México"):
        self.pais = pais

    def capitalize(self):
        if self.pais in self.capitales:
            return self.capitales[self.pais]
        else:
            return 'País desconocido'


def capital(objeto):
    return objeto.capitalize()

pais = CapitalesMundiales("Bolivia")
mensaje = "HOLA"

print capital(pais)
print capital(mensaje)
