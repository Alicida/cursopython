#! /bin/bash
# -*- coding: utf-8 -*-
"""Ejecuta un pequeño programa de ejemplo con diversas clases."""
import clases_dispositivos
print 'Creamos un dispositivo con nombre "Radio"...'
radio = clases_dispositivos.Dispositivo("Radio")
print 'Encedemos a %s...' % radio.nombre
radio.encendido = True
print "El dispositivo %s está %s." % (radio.nombre, radio.estado())
clases_dispositivos.Dispositivo.conteoDisp()
print '\nCreamos un dispositivo con nombre "TV"...'
televisor = clases_dispositivos.Dispositivo("TV")
clases_dispositivos.Dispositivo.conteoDisp()
print '\nCreamos un dispositivo con nombre "TabletPC"...'
Mi_tablet = clases_dispositivos.Tablet("TabletPC")
clases_dispositivos.Dispositivo.conteoDisp()
print "\nAhora destruimos el objeto %s." % radio.nombre
del radio
clases_dispositivos.Dispositivo.conteoDisp()
mensaje = "\nPresionar <Enter> El programa termina y los objetos se destruyen."
raw_input(mensaje)