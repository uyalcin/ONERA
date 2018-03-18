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
length = form.getvalue('l')
width = form.getvalue('w')
height = form.getvalue('h')
percentFillingBox = form.getvalue('percent')
nbObjects = form.getvalue('nb')

l = int(length)
w = int(width)
h = int(height)
p = float(percentFillingBox)
n = int(nbObjects)

#fonction qui fait directement tout et qui renvoie le dico contenant infos sur placement boites
#d2 = liaisonDatas(l, w, h, p, n)

conteneur, boxList = generateurObjets(l, w, h, p, n)
#tableau double dimension contenant toutes les informations des boxs
objectsList = changeList(boxList)
#dictionnaire contenant toutes les coordonnées des boites dans le conteneur
d2 = callSolveur(conteneur, boxList)

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Dude</title>')
print ('</head>')
print ('<body>')
print ("<h2>Box : (%s,%s,%s)</h2>" % (l, w, h))
print ("<h2>Percent -> %s  ~  Number -> %s</h2>" % (p, n))
print ("<h2>%s</h2>" % (l))
print ("<h2>chemin : %s</h2>" % (abspath))
#for k in d2:
#	print ("<h2>Box %s : (%s,%s,%s) -> (%s,%s,%s)</h2>" % (k["id"], k["coordinates"]["x1"], k["coordinates"]["y1"], k["coordinates"]["z1"], k["coordinates"]["x2"], k["coordinates"]["y2"], k["coordinates"]["z2"]))
#for line in objectsList:
#	print ("<h2>[%s,%s,%s,%s,%s]" % (line[0], line[1], line[2], line[3], line[4]))
print ("</body>")
print ("</html>")

