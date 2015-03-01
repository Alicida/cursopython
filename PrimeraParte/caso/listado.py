#! /usr/bin/python
# -*- coding: utf-8 -*-
import datos


def lista():
    contador = 0
    for alumno in datos.alumnos:
        contador += 1
        print "\nAlumno: ", contador
        for identificador in datos.orden:
            print identificador + ": " + str(alumno[identificador])
