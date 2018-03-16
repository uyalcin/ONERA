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

liaisonDatas(l, w, h, p, n)

print ("Content-type:text/html\r\n\r\n")
print ('<html>')
print ('<head>')
print ('<title>Hello Dude</title>')
print ('</head>')
print ('<body>')
print ("<h2>Box : (%s,%s,%s)</h2>" % (l, w, h))
print ("<h2>Percent -> %s  ~  Number -> %s</h2>" % (p, n))
print ("<h2>chemin : %s</h2>" % (abspath))
print ("</body>")
print ("</html>")


