#secreto_heredado
# -*- coding: utf-8 -*-
#! /usr/bin/python
"""Módulo que contiene dos clases con atributos de accesorestringido mediante
name mangling heredados."""

import secreto


class DobleSeguridad(secreto.Confidencial):
    """Sistema con doble factor de seguridad. Subclase de Confidencial."""

    def __init__(self, nombre, usuario, password_1, password_2):
        self.segundo_factor = password_2
        print "Bienvenido a %s." % nombre
        super(DobleSeguridad, self).__init__(usuario, password_1)

    def acceso(self, usuario, password_1, password_2):
        """Método al que se accede a los secretos del sistema con doble factor
        de seguridad."""
        if usuario == self.usuario and password_1 == self.password and \
        password_2 == self.segundo_factor:
            self._Confidencial__ultimaBarrera()
        else:
            print "Acceso denegado."
        return


if __name__ == "__main__":

    balija = secreto.Confidencial("Bond", "007")
    print "... \n..."
    print"Para abrir la balija diplomática..."
    usuario = raw_input("Ingrese su usuario: ")
    password = raw_input("Ingrese su contraseña: ")
    balija.acceso(usuario, password)
    print "... \n..."
    palacio = DobleSeguridad("Palacio de Buckingham", "Bond", "007",
        "Skyfall")
    print "... \n..."
    hackeado = palacio._Confidencial__password_maestro
    print "¡Anonymous nos acaba de hackear!"
    print "El código maestro es ''%s''." % hackeado
    print "... \n..."

    usuario = raw_input("Ingrese su usuario: ")
    password = raw_input("Ingrese su contraseña: ")
    segundo_factor = raw_input("Ingrese segundo factor de seguridad: ")
    palacio.acceso(usuario, password, segundo_factor)