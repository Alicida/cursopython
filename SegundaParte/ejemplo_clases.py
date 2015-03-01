#! /usr/bin/python
# -*- coding: utf-8 -*-
'''ejemplo_clases.py es un archivo que contiene la definición de varias clases
   "Dispositivo", la cual nos sirve de ejemplo para el uso de la
   programación orientada a objetos'''


class Dispositivo():
    '''La clase Dispositivo define un dispositivo simple
    que se puede prender o apagar.'''
    numero = 0

    def __init__(self, nombre):
        '''El método __init__ inicializa valores y variables una vez que se
        crea un objeto. En este caso, se suma 1 a la variable estática
        Dispositivo.numero, se define la variable self.encendido como False y
        despliega información.'''
        self.encendido = False
        '''Dentro de los métodos es posible definir y llamar variables propias
        del objeto con el prefijo self.'''
        self.nombre = nombre
        print self.nombre
        print self.estado()
        print
        Dispositivo.numero += 1  # Dispositivo.número es un campo estático.

    def estado(self):
        '''El método estado regresa una cadena indicando si el dispositivo
        está encendido.'''
        if self.encendido:
            return "Encendido"
        else:
            return "Apagado"

    def __del__(self):
        '''El método __del__ se ejecuta cuando el objeto es desechado.
        En este caso, al ser desechado el objeto instanciado, se le restará a
        la variable estática Dispositivo.numero 1 unidad.'''
        print "El dispositivo %s se ha descompuesto." % self.nombre
        Dispositivo.numero -= 1

    @staticmethod
    def conteoDisp():
        '''conteoDisp es un método estático que despliega el valor de
        Dispositivo.numero.'''
        print "Hay %d dispositivos actualmente" % Dispositivo.numero


class RadioDesp(Dispositivo):
    '''RadioDesp es una clase heredada de la clase Dispositivo
    con la añadidura del método alarma()'''
    hora_alarma = "12:30"  # Hora de la alarma por defecto.

    def alarma(self, hora):
        '''alarma es un método que comprueba si el dispositivo se encuentra
        encendido y a partir de la comparación de la variable self.hora_alarma
        y del parámetro hora, envía un mensaje específico.'''
        if not self.encendido:
            print "zzzzzzzz...zzzzzzz"
        elif hora == self.hora_alarma:
            print "ring... ring"
        else:
            print "sigue durmiendo"

    def poner_alarma(self, hora):
        '''poner_alarma es un método que modifica la variable self.hora_alarma
        siempre y cuando la variable self.encendido sea cierta.'''
        if self.encendido:
            self.hora_alarma = hora
            print "La alarma está puesta a las %s." % self.hora_alarma
        else:
            print "zzzzzzzz...zzzzzzz"


class Tablet(RadioDesp):
    '''La clase Tablet es una clase heredada de radio despertador.'''

    def __init__(self, nombre):
        '''El método __init__ sobreescribe al método heredado de la clase
        superior. En este caso, self.numero es una cadena de texto y
        no un número, además de que no se incrementa en 1 la variable
        estática Dispositivo.numero'''
        self.numero = "No soy un dispositivo, soy una tablet."
        self.nombre = nombre
        self.encendido = False

    def __del__(self):
        '''El método __del__ sobreecribe al método heredado de la clase
        superior. Debido a ello, la disminución en 1 de la variable estática
        Dispositivo.numero'''
        pass


def prueba():
    """Ejecuta un pequeño programa de ejemplo"""
    radio = Dispositivo("radio")
    radio.encendido = True
    print radio.estado()
    print Dispositivo.numero
    print
    televisor = Dispositivo("TV")
    print Dispositivo.numero
    Dispositivo.conteoDisp()
    del radio
    Mi_ipad = Tablet("El iPad")
    print Mi_ipad.numero
    Dispositivo.conteoDisp()
    del Mi_ipad
    Dispositivo.conteoDisp()


def prueba_nueva():
    print "Consiguiendo el despertador."
    mi_despertador = RadioDesp("Panasonic")
    print "Poniendo la alarma a las 12:45..."
    mi_despertador.poner_alarma("12:45")
    print "¡Ups! El despertador está apagado."
    print "Prendiendo el despertador..."
    mi_despertador.encendido = True
    print "¿Cuál es el estado del despertado?"
    print mi_despertador.estado()
    print "Son las 11:30"
    mi_despertador.alarma("11:30")
    print "La alarma está puesta a las %s." % (mi_despertador.hora_alarma)
    print "Poniendo la alarma a las 12:45."
    mi_despertador.poner_alarma("12:45")
    print "Son las 12:45..."
    mi_despertador.alarma("12:45")
