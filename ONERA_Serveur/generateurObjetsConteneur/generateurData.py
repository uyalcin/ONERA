# -*- coding: utf-8 -*-

from __future__ import division #pour avoir une division avec float !!

import os
import sys
import random 
import math


from objet import *
from conteneur import *

#repartition pous savoir combien on aura de gros, moyens et petits objets au total (on retourne une liste)
#exemple tab[4,5,6] -> signification : 4 gros objets, 5 petits et 6 moyens 
def repartition (nb, vol, percent):
	volVoulu = vol * percent
	repartitionTab = []
	
	if nb > 10 : #meilleur repartition si nb > 10
		#on calcule le nbre d'objets lourds
		rand1 = random.randint(math.floor(0.2 * nb), math.floor(0.8 * nb))
		#print(rand1)
		if nb-rand1 < rand1 :
			repartitionTab.append(nb-rand1)
			reste = rand1
		else :
			repartitionTab.append(rand1)
			reste = nb - rand1
		
		#on calcule le nbre d'objets legers puis moyens avec le nb qu'il reste 
		#print("reste : {}".format(reste))
		if reste > 10:
			rand2 = random.randint(math.floor(0.2 * reste), math.floor(0.8 * reste))
			#print(rand2)
			if reste-rand2 < rand2 :
				repartitionTab.append(reste-rand2)
				repartitionTab.append(rand2)
			else :
				repartitionTab.append(rand2)
				repartitionTab.append(reste - rand2)
		else :
			rand2 = random.randint(0, reste)
			if reste-rand2 < rand2 :
				repartitionTab.append(reste-rand2)
				repartitionTab.append(rand2)
			else :
				repartitionTab.append(rand2)
				repartitionTab.append(reste - rand2)
				
	else :
		rand1 = random.randint(math.floor(0.1 * nb), math.floor(0.9 * nb))
		if nb-rand1 < rand1 :
			repartitionTab.append(nb-rand1)
			reste = rand1
		else :
			repartitionTab.append(rand1)
			reste = nb - rand1
			
		rand2 = random.randint(0, reste)
		if reste-rand2 < rand2 :
			repartitionTab.append(reste-rand2)
			repartitionTab.append(rand2)
		else :
			repartitionTab.append(rand2)
			repartitionTab.append(reste - rand2)
	
	return repartitionTab
	
#Cette fonction va créer tous les objets à partir d'une liste de volume pour chaque objet ... 
def listeObjets (tabVol, conteneur, volumeMoyen):
	"""
	minLon = conteneur.longueur * 0.2
	maxLon = conteneur.longueur * 0.27
	minLar = conteneur.largeur * 0.2
	maxLar = conteneur.largeur * 0.27
	
	print("Longueur [{} ; {}] et Largeur [{} ; {}]".format(minLon, maxLon, minLar, maxLar))
	"""
	
	tabObjets = []
	numObj = 0
	
	for e in tabVol:
		if e > volumeMoyen * 1.2 : #gros objet
			randLon = random.randint(math.floor(conteneur.longueur * 0.38), math.floor(conteneur.longueur * 0.45))
			randLar = random.randint(math.floor(conteneur.largeur * 0.38), math.floor(conteneur.largeur * 0.45))
			hau = e / (randLar*randLon)
			#print("Gros : {}, [{} ; {} ; {}]".format(e, randLon, randLar, hau))
		elif e > volumeMoyen * 0.8 : #objet moyen
			randLon = random.randint(math.floor(conteneur.longueur * 0.32), math.floor(conteneur.longueur * 0.38))
			randLar = random.randint(math.floor(conteneur.largeur * 0.32), math.floor(conteneur.largeur * 0.38))
			hau = e / (randLar*randLon)
			#print("Moyen : {}, [{} ; {} ; {}]".format(e, randLon, randLar, hau))
		else : #petit objet
			if (len(tabVol) > 40) :
				randLon = random.randint(math.floor(conteneur.longueur * 0.20), math.floor(conteneur.longueur * 0.32))
				randLar = random.randint(math.floor(conteneur.largeur * 0.28), math.floor(conteneur.largeur * 0.32))
				hau = e / (randLar*randLon)
			else :
				randLon = random.randint(math.floor(conteneur.longueur * 0.28), math.floor(conteneur.longueur * 0.32))
				randLar = random.randint(math.floor(conteneur.largeur * 0.28), math.floor(conteneur.largeur * 0.32))
				hau = e / (randLar*randLon)
			
		cpt = 0
		while hau > conteneur._get_hauteur() and cpt < 100:
			if randLon+1 < conteneur._get_longueur() :
				randLon +=1
			if randLar +1 < conteneur._get_largeur() :
				randLar +=1
			hau = e / (randLar*randLon)
				
			cpt += 1
			
		if cpt == 100:
			print("ATTENTION, probleme d'objet avec hauteur !!!")
				
		obj = Objet(numObj ,randLon, randLar, math.floor(hau), 0)
		tabObjets.append(obj)
		numObj += 1
			
			#print("Petit : {}, [{} ; {} ; {}]".format(e, randLon, randLar, hau))
	#print(tabObjets)
	return tabObjets

#Cette fonction créer tous les objets en fonction de la liste fournie (x gros, y legers et z moyens)
def creationObjets (tab, conteneur, volumeMoyen, pourcentage) : 
	nbGros = tab[0]
	nbPetits = tab[1]
	nbMoyens = tab[2]
	
	tabVol = []
	vol = conteneur.volumeTot()
	while vol >= conteneur.volumeTot() * (pourcentage + 0.1) :
		tabVol = []
		for i in range (nbGros):
			rand = random.randint(math.floor(volumeMoyen * 1.2),math.floor(volumeMoyen * 1.6))
			tabVol.append(rand)
		
		for i in range (nbPetits):
			rand = random.randint(math.floor(volumeMoyen * 0.4),math.floor(volumeMoyen * 0.8))
			tabVol.append(rand)
		
		for i in range (nbMoyens):
			rand = random.randint(math.floor(volumeMoyen * 0.8),math.floor(volumeMoyen * 1.2))
			tabVol.append(rand)
			
		
		vol = 0
		for e in tabVol:
			vol += e
			
	tab = listeObjets (tabVol, conteneur, volumeMoyen)
		
	return tab
	
	
#definition des poids des objets de la liste
#poids compris entre 20 et 200KG (arbitraire)
def definirPoids (liste, volConteneur) :
	nbObjets = len(liste)
	cptPetit = 0
	cptGros = 0
	for o in liste :
		#afin de savoir ou se situe notre objet qq soit le nbre d'obj demandés ... 
		valTemp = o.volumeTot()*100*nbObjets / volConteneur 
		
		if (valTemp < 50) : #objets petits (plus ou moins)
			if cptPetit % 4 == 0 :
				rand = random.randint(80, 160)
			else :
				rand = random.randint(20, 120)
			o._set_poids(rand)
			cptPetit += 1
		elif (valTemp < 90) : #objets moyens (plus ou moins)
			rand = random.randint(50, 170)
			o._set_poids(rand)
		else : #objets gros (plus ou moins)
			if cptGros % 4 == 0 :
				rand = random.randint(40, 120)
			else :
				rand = random.randint(100, 200)
			o._set_poids(rand)
			cptGros += 1
		
	return liste
	
#Créer un generateur qui ne depasse pas la quantite totale possible et qui genere en fonction du nombre d'objets voulus ... 
#generer des objets de telle sorte qu'ils remplissent un certain pourcentage du conteneur
def generationObjets1 (conteneur, nbreObjVoulus, pourcentage):
	if  pourcentage > 1 or pourcentage < 0  or nbreObjVoulus < 1: #verification que nous avons un pourcentage et nbreObjVoulus coherents
		return []
	else :
		liste = [] #Liste des objets !
		volume = conteneur.volumeTot()
		repartitionTab = repartition(nbreObjVoulus, volume, pourcentage)
		volumeMoyen = volume * pourcentage / nbreObjVoulus
		
		#print("Volume moyen : {} cm3, {} m3".format(volumeMoyen, volumeMoyen / 1000000))
		#print(repartitionTab)
		#print("Volume Total : {} cm3, {} m3".format(volume, volume / 1000000))
		
		listeObjet = []
		while (listeObjet == [] or verificationCapacite(conteneur, listeObjet) == False) :
			listeObjet = creationObjets(repartitionTab, conteneur, volumeMoyen, pourcentage)
		#Calcul du volume total de tous les objets afin de verifier que ca ne depasse pas la capacité totale du conteneur !!
		
		listeObjet = definirPoids (listeObjet, volume)
		
		#print("\nListe des objets : ")
		#for o in listeObjet:
		#	print(o)
		
	return listeObjet
	
#generer des objets de telle sorte que la volume tot ne depasse pas le volume du conteneur ... 
#def generationObjets2 (conteneur, nbreObjVoulus):




def verificationCapacite (conteneur, liste):
	volumeTot = conteneur.volumeTot()
	
	volumeObj = 0
	for o in liste:
		volumeObj += o.volumeTot()
		#print(o.volumeTot())
		
	#print("\nLes objets occupent {}% de l'espace total".format(volumeObj*100 / conteneur.volumeTot()))
	return volumeObj < volumeTot
	#print ("Volumen totale : {}".format(volumeTot))
	
	



	
	
