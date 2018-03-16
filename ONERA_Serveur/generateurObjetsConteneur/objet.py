# -*- coding: utf-8 -*-

import os
import sys
import random
import pickle

class Objet:
	nbreObjets = 0
	
	def __init__ (self, num, longueur, largeur, hauteur, poids) :
		self._num = num
		self._longueur = longueur
		self._largeur = largeur
		self._hauteur = hauteur
		self._poids = poids
		
		
		
		Objet.nbreObjets += 1
	def _get_num (self):
		return self._num
		
	def _set_num (self, num) :
		self._num = num
		
	num = property(_get_num, _set_num)
		
	def _get_longueur (self):
		return self._longueur
		
	def _set_longueur (self, lon) :
		self._longueur = lon
		
	longueur = property(_get_longueur, _set_longueur)
	
	def _get_largeur (self):
		return self._largeur
		
	def _set_largeur (self, lar) :
		self._largeur = lar
		
	largeur = property(_get_largeur, _set_largeur)
	
	def _get_hauteur (self):
		return self._hauteur
		
	def _set_hauteur (self, hau) :
		self._hauteur = hau
		
	hauteur = property(_get_hauteur, _set_hauteur)
	
	def _get_poids (self):
		return self._poids
		
	def _set_poids (self, p) :
		self._poids = p
		
	poids = property(_get_poids, _set_poids)
	
	def volumeTot (self):
		return self.longueur * self.largeur * self.hauteur
		
	def combien (cls):
		print ("Nbre d'objets : {}".format(cls.nbreObjets))
	combien = classmethod(combien)
	
	def __repr__(self):
		return "Objet {} : Longueur -> {}, Largeur -> {}, Hauteur -> {}, Poids -> {} Kg, ({} m3)".format(self.num, self.longueur, self.largeur, self.hauteur, self.poids, self.longueur * self.largeur * self.hauteur / 1000000)