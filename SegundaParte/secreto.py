# -*- coding: utf-8 -*-
#! /usr/bin/python
"""Módulo que contiene una clases con atributos de acceso restringido."""


class Confidencial(object):
    """Esta clase crea objetos con una contraseña maestra."""
    __password_maestro = "123qwe"

    def __init__(self, usuario, password):
        """Método que asigna un usuario y contraseña inicial."""
        self.usuario = usuario
        self.password = password
        print "*click*... Dispositivo armado."

    def acceso(self, usuario, password):
        """Método al que se accede a los secretos del sistema."""
        if usuario == self.usuario and password == self.password:
            self.__ultimaBarrera()
        else:
            print "Acceso denegado."
        return

    def __ultimaBarrera(self):
        """Validación antes de acceder a los secretos."""
        clave = raw_input("Ingrese código maestro: ")
        if clave == self.__password_maestro:
            print ("Ahora tiene acceso a nuestros secretos.")
        else:
            print "¡KA-BOOOM!"
        return

if __name__ == "__main__":
    caja_fuerte = Confidencial("Bond", "Moneypenny")
    usuario = raw_input("Ingrese su usuario: ")
    password = raw_input("Ingrese su contraseña: ")
    caja_fuerte.acceso(usuario, password)
    print "... \n... \n..."


    hackeado = caja_fuerte._Confidencial__password_maestro
    print "¡Anonymous nos acaba de hackear!"
    print "El código maestro es ''%s''." % hackeado

    caja_fuerte._Confidencial__ultimaBarrera()