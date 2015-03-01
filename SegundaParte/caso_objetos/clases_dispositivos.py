#! /usr/bin/python
# -*- coding: utf-8 -*-
'''ejemplo_clases.py es un archivo que contiene la definición de varias clases
   "Dispositivo", la cual nos sirve de ejemplo para el uso de la
   programación orientada a objetos'''


class Dispositivo(object):
    '''La clase Dispositivo define un dispositivo simple
    que se puede prender o apagar.'''
    numero = 0

    def __init__(self, nombre):
        '''El método __init__ inicializa valores y campos una vez que se
        crea un objeto. En este caso, se suma 1 al campo estático
        Dispositivo.numero, se define el campo self.encendido como False y
        despliega información.'''
        Dispositivo.numero += 1  # Dispositivo.número es un campo estática.
        self.numero + Dispositivo.numero
        self.encendido = False
        self.nombre = nombre
        print "%s, creado con el número %d." % (self.nombre, self.numero)
        print "%s está %s." % (self.nombre, self.estado())

    def estado(self):
        '''El método estado regresa una cadena indcando si el dispositivo
        está encendido a partir del estado del campo self.encendido.'''
        if self.encendido:
            return "Encendido"
        else:
            return "Apagado"

    def __del__(self):
        '''El método __del__ se ejecuta cuando el objeto es desechado.
        En este caso, al ser desechado el objeto instanciado, se le restará 1
        al campo estático Dispositivo.numero.'''
        print "El objeto clase Dispositivo %s se ha destruido." % self.nombre
        Dispositivo.numero -= 1

    def conteoDisp():
        '''conteoDisp es un método estático que despliega el valor de
        Dispositivo.numero.'''
        print "Hay %d dispositivos actualmente." % Dispositivo.numero
    conteoDisp = staticmethod(conteoDisp)


class RadioDesp(Dispositivo):
    '''RadioDesp es una clase heredada de la clase Dispositivo
    con la añadidura del método alarma()'''
    hora_alarma = "12:30"  # Hora de la alarma por defecto.

    def alarma(self, hora):
        '''alarma es un método que comprueba si el dispositivo se encuentra
        encendido y a partir de la comparación del campo self.hora_alarma
        y del parámetro hora, envía un mensaje específico.'''
        if not self.encendido:
            print "zzzzzzzz...zzzzzzz"
        elif hora == self.hora_alarma:
            print "¡RIIING... RIIING!"
        else:
            print "Sigue durmiendo."
            print "La alarma está puesta a las %s." % (self.hora_alarma)

    def poner_alarma(self, hora):
        '''poner_alarma es un método que modifica el campo self.hora_alarma
        siempre y cuando el campo self.encendido sea cierto.'''
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
        no un número, además de que no se incrementa en 1 el campo
        estática Dispositivo.numero'''
        self.numero = "La tablet no se suma a los dispositivos"
        self.nombre = nombre
        self.encendido = False
        print "%s, creado. %s." % (self.nombre, self.numero)
        print "%s está %s." % (self.nombre, self.estado())

    def __del__(self):
        '''El método __del__ sobreecribe al método heredado de la clase
        superior. Debido a ello, la disminución en 1 del campo estático
        Dispositivo.numero'''
        print "El objeto clase Tablet % s se ha destruido." % self.nombre