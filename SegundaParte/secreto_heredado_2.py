#secreto_heredado
# -*- coding: utf-8 -*-
#! /usr/bin/python
"""Módulo que contiene dos clases con atributos de acceso restringido.
Esta versión sobreescribe los atributos escondidos mediante name mangling."""


class Confidencial(object):
    """Esta clase crea objetos con una contraseña maestra."""
    __password_maestro = "123qwe"

    def __init__(self, usuario, password):
        """Método que asigna un usuario y contraseña inicial."""
        self.usuario = usuario
        self.password = password
        print "*click*... Dispositivo armado."

    def __ultimaBarrera(self):
        """Validación de constraseña maestra para de acceder a los secretos."""
        clave = raw_input("Ingrese código maestro: ")
        if clave == self.__password_maestro:
            print ("Ahora tiene acceso a nuestros secretos.")
        else:
            print "¡KA-BOOOM!"
        return

    def acceso(self, usuario, password):
        """Método al que se accede a los secretos del sistema."""
        if usuario == self.usuario and password == self.password:
            self.__ultimaBarrera()
        else:
            print "Acceso denegado."
        return


class DobleSeguridad(Confidencial):
    """Sistema con doble factor de seguridad.
    Es una subclase de Confidencial()."""
    __password_maestro = "qwe123"  # Sobreescribe al campo de Confidencial().

    def __init__(self, nombre, usuario, password_1, password_2):
        self.segundo_factor = password_2
        print "Bienvenido a %s." % nombre
        super(DobleSeguridad, self).__init__(usuario, password_1)

    def __ultimaBarrera(self):
        """Validación de la contraseña maestra para acceder a los secretos.
        Este método sobreescribe al que se encuentra en
        la clase Confidencial()."""
        clave = raw_input("Ingrese código maestro: ")
        if clave == self.__password_maestro:
            print ("Ahora tiene acceso a nuestros secretos.")
        else:
            print "¡KA-BOOOM!"
        return

    def acceso(self, usuario, password_1, password_2):
        """Método al que se accede a los secretos del sistema con doble factor
        de seguridad."""
        if usuario == self.usuario and password_1 == self.password and \
        password_2 == self.segundo_factor:
            self.__ultimaBarrera()
        else:
            print "Acceso denegado."
        return


if __name__ == "__main__":

    balija = Confidencial("Bond", "007")
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
    print "... \n..."
    hackeado = palacio._DobleSeguridad__password_maestro
    print "¡Anonymous corrigió!"
    print "El código maestro es ''%s''." % hackeado