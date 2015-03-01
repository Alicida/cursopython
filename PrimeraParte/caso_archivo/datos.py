#! /usr/bin/python
# -*- coding: utf-8 -*-

#El valor de ruta es la ruta donde se encuentra el archivo datos.txt
#Ejemplo en Windows: "C:\Users\Josech\Documentos\Python\datos.txt"
ruta = "/home/josech/Documentos/Cursos/Contenidos/Python/Introduccion_a_Python\
/codigo_nuevo/caso_archivo/datos.txt"

orden = ("Nombre", "Primer Apellido", "Segundo Apellido", "Carrera",
"Semestre", "Promedio", "Al Corriente")

campos = {"Nombre": str, "Primer Apellido": str, "Segundo Apellido": str,
         "Carrera": str, "Semestre": int, "Promedio": float,
         "Al Corriente": bool}

carreras = ("Sistemas", "Derecho", "Actuaría", "Arquitectura",
    "Administración")
