#! /usr/bin/python
# -*- coding: utf-8 -*-
import datos


def carga_datos(ruta):
    data = []
    with open(ruta, "r") as archivo:
        lineas = archivo.readlines()
    for linea in lineas:
        dato = eval(linea)
        data.append(dato)
    return data


def lista():
    alumnos = carga_datos(datos.ruta)
    contador = 0
    for alumno in alumnos:
        contador = contador + 1
        print "\nAlumno: ", contador
        for identificador in datos.orden:
            print identificador + ": " + str(alumno[identificador])
