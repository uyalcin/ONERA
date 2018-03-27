#! /usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys

# Import des modules pour gérer CGI 
import cgi, cgitb 

if os.name == 'posix':
	abspath = os.path.dirname(os.path.realpath(__file__))
	cpt = 0
	while (cpt != 2):
		if abspath[-1:] == '/':
			cpt += 1
		abspath = abspath[:-1]

	sys.path.insert(0, abspath+'/')
	from appel import *
	

# Crée une instance pour récupérer les réponses d'un formulaire
form = cgi.FieldStorage() 
# Récupère les données depuis les champs du formulaire
length = form.getvalue('length')
width = form.getvalue('width')
height = form.getvalue('height')
percentFillingBox = form.getvalue('percentFillingBox')
nbObjects = form.getvalue('numberObjectsWanted')

l = int(length)
w = int(width)
h = int(height)
p = float(percentFillingBox)
n = int(nbObjects)

if p > 0.8 :
	p = 0.8

#fonction qui fait directement tout et qui renvoie le dico contenant infos sur placement boites
#d2 = liaisonDatas(l, w, h, p, n)

conteneur, boxList = generateurObjets(l, w, h, p, n)
#tableau double dimension contenant toutes les informations des boxs
objectsList = changeList(boxList)
#dictionnaire contenant toutes les coordonnées des boites dans le conteneur
d2 = callSolveur(conteneur, boxList)

print ("Content-type:text/html\r\n")
for k in d2:
	print ("%s,%s,%s,%s,%s,%s" % (k["coordinates"]["x1"], k["coordinates"]["y1"], k["coordinates"]["z1"], k["coordinates"]["x2"], k["coordinates"]["y2"], k["coordinates"]["z2"]))
#for line in objectsList:
#	print ("<h2>[%s,%s,%s,%s,%s]" % (line[0], line[1], line[2], line[3], line[4]))


#192.168.43.93:8000/server/process.py?length=20&width=20&height=20&percentFillingBox=0.6&numberObjectsWanted=20
