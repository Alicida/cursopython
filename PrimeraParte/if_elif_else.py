#! /usr/bin/python
# -*- coding: utf-8 -*-

animal = raw_input("¿Qué animal sugiere? ")
print "Este animal es %s." % animal
if animal == "gato":
    print "miau"
elif animal == "perro":
    print "guau"
elif animal == "pez":
    print "glub glub"
elif animal == "gallo":
    print "kikiriki"
elif animal == "vaca":
    print "muuu"
else:
    print "No sé que ruido hace este animal."
print "Sólo los gatos maullan."
