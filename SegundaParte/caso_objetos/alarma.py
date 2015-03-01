#! /bin/bash
# -*- coding: utf-8 -*-
"""Ejecuta un pequeño programa de ejemplo del uso de los objetos clase
Radio.Desp"""
import clases_dispositivos
print 'Creando el objeto "Despertador"...'
mi_despertador = clases_dispositivos.RadioDesp("Despertador")
print "\nPoniendo la alarma a las 12:45..."
mi_despertador.poner_alarma("12:45")
print "¡Ups! El despertador está apagado..."
print "\nPrendiendo el despertador..."
mi_despertador.encendido = True
print "\n¿Cuál es el estado del despertador?"
print mi_despertador.estado()
print "\nSon las 11:30..."
mi_despertador.alarma("11:30")
print "\nPoniendo la alarma a las 12:45..."
mi_despertador.poner_alarma("12:45")
print "\nSon las 12:45..."
mi_despertador.alarma("12:45")