#! /usr/bin/python
# -*- coding: utf-8 -*-

versiones = {"Ubuntu": "12.10", "Mac OS X": "10.8", "Debian": "6.06",
"CentOS": "6.4"}
print "Despliega el diccionario."
print versiones.items()
print
print "Despliega los identificadores del diccionario."
print versiones.keys()
print
print "Despilega los valores del diccionario."
print versiones.values()
print
print "Despliega cada par (identificador, valor) del diccionario."
for item in versiones.iteritems():
    print item
print
print "Despliega cada identificador del diccionario."
for identificador in versiones.iterkeys():
    print identificador
print
print "Despliega cada valor del diccionario."
for valor in versiones.itervalues():
    print valor
