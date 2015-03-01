#! /usr/bin/python
# -*- coding: utf-8 -*-
import altas
import listado
import datos

excepcion = True
while excepcion:
    excepcion = False
    try:
        alumnos = raw_input("Número de alumnos: ")
        alumnos = int(alumnos)
        print
    except (ValueError) as error:
        print error
        excepcion = True

for contador in range(alumnos):
    print "\nAlumno nuevo", contador + 1
    nuevo_alumno = altas.alta()
    with open(datos.ruta, "a") as archivo:
        archivo.write(str(nuevo_alumno) + "\n")

listado.lista()
