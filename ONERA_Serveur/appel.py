import os
import sys

from operator import attrgetter

#print(os.path.abspath(os.path.dirname(__file__)+'/testAPI/'))
#print(os.path.dirname(os.path.realpath(__file__))+'/testAPI/')
#print(os.path.dirname(os.path.realpath(__file__))+'/generateurObjetsConteneur/')

#WINDOWS
#sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)+'/generateurObjetsConteneur/'))

#LINUX
if os.name == 'posix':
	sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/generateurObjetsConteneur/')
	from objet import *
	from conteneur import *
	from generateurData import *
	
	#sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/solveur3D/')
	#from repartitionObjets import *

	sys.path.insert(0, os.path.dirname(os.path.realpath(__file__))+'/testAPI/')
	from test import *

else : #sous windows
	sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)+'/generateurObjetsConteneur/'))
	from objet import *
	from conteneur import *
	from generateurData import *

	#sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)+'/solveur3D/'))
	#from repartitionObjets import *

	sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)+'/testAPI/'))
	from test import *



def comp (v1, v2):
	a = v1._get_poids()
	b = v2._get_poids()
	if  a<b :
		return -1
	elif a>b :
		return 1
	else :
		return 0

def  solveurSansContraintes (conteneur, l):
	listeItems = []
	for o in l :
		new = dict()
		new["w"] = o._get_largeur()
		new["h"] = o._get_hauteur()
		new["d"] = o._get_longueur()
		new["q"] = 1
		new["vr"] = 1
		new["wg"] = o._get_poids()
		new["id"] = o._get_num()
		listeItems.append(new)
	#print listeItems
	
	
	listeConteneur = []
	
	newCont = dict()
	newCont = {"w": conteneur._get_largeur(), "h": conteneur._get_hauteur(), "d": conteneur._get_longueur(), "max_wg": 0, "id": "Conteneur1"}
	listeConteneur.append(newCont)
	#print newCont
	
	#solveur3D()
	positionObjets =  solveur3D(listeConteneur, listeItems)

	return positionObjets

	
def sameLevel (l):
	"""
	for k in l:
		print "{} -> ({}, {}, {}) - ({}, {}, {})".format(k["id"], k["coordinates"]["x1"], k["coordinates"]["y1"], k["coordinates"]["z1"], k["coordinates"]["x2"], k["coordinates"]["y2"], k["coordinates"]["z2"])
	print"\n"
	"""
	for o in l:
		if o["coordinates"]["y1"] > 0: #verifier qu'ils sont tous au meme niveau !!
			return False
	
	
	return True
	
"""
	listeRetournee = []
	
	for k in d2:
		print "{} -> ({}, {}, {}) - ({}, {}, {})".format(k["id"], k["coordinates"]["x1"], k["coordinates"]["y1"], k["coordinates"]["z1"], k["coordinates"]["x2"], k["coordinates"]["y2"], k["coordinates"]["z2"])
"""
	
def solveurPoidsContrainte (conteneur, l):
	#Tri de la liste en fonction du poids !
	listeTrieePoids = sorted(l, key=lambda e : e.poids, reverse = True)
	"""
	print "\n"
	for o in listeTrieePoids:
		print o
	"""
	listeConteneur = []
	
	newCont = dict()
	newCont = {"w": conteneur._get_largeur(), "h": conteneur._get_hauteur(), "d": conteneur._get_longueur(), "max_wg": 0, "id": "Conteneur1"}
	listeConteneur.append(newCont)
	
	cpt1 = 0
	cpt2 = 0
	listeEnvoi = []
	tmp = []
	listeLevel = []
	while (cpt2 != len(listeTrieePoids) -2):
		cpt1 = cpt2
		cpt2 += 1
		tmp = []
		listeEnvoi = []
		while (sameLevel(listeEnvoi) and cpt2 < len(listeTrieePoids)):
			tmp = listeTrieePoids[cpt1:cpt2]
			#print tmp
			listeItems = []
			listeEnvoi = []
			for o in tmp :
				new = dict()
				new["w"] = o._get_largeur()
				new["h"] = o._get_hauteur()
				new["d"] = o._get_longueur()
				new["q"] = 1
				new["vr"] = 1
				new["wg"] = o._get_poids()
				new["id"] = o._get_num()
				listeItems.append(new)
				
			listeEnvoi = solveurLevel3D (listeConteneur, listeItems)
			cpt2 += 1
		
		#print cpt2-cpt1-2
		listeLevel.append(cpt2-cpt1-2)
		cpt2 -= 2
		
	listeLevel[len(listeLevel)-1] += 1
	print listeLevel
		
		
def liaisonCpp ():
	conteneur = Conteneur(40,40,70)
	l = generationObjets1(conteneur, 20, 0.6)
	#Appel solveur sans contraintes
	solveurSansContraintes(conteneur, l)

def liaisonDatas (l, w, h, percentFillingBox, nbObjects):
	conteneur = Conteneur(l, w, h)
	l = generationObjets1(conteneur, nbObjects, percentFillingBox)
	#Appel solveur sans contraintes
	positionObjets = solveurSansContraintes(conteneur, l)
	#print len(positionObjets)
	return positionObjets
	
		
if __name__ == "__main__":
	#on travaille en cm pour plus de facilite 
	#conteneur = Conteneur(100,75,150)
	conteneur = Conteneur(40,40,70)
	l = generationObjets1(conteneur, 20, 0.6)

	#Appel solveur sans contraintes
	solveurSansContraintes(conteneur, l)

	#Appel solveur avec 1 contrainte (poids)
	#solveurPoidsContrainte(conteneur, l)
	
	
	
	
	
	
	
	
	
	
	
	
	
