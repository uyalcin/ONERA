# -*- coding: utf-8 -*-

import os
import sys

class Conteneur:
	
	def __init__ (self, longueur, largeur, hauteur) :
		self._longueur = longueur
		self._largeur = largeur
		self._hauteur = hauteur

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
	
	def volumeTot (self):
		return self.longueur * self.largeur * self.hauteur
	
	def __str__ (self):
		return ("Conteneur : Longueur -> {}, Largeur -> {}, Hauteur -> {}".format(self.longueur, self.largeur, self.hauteur))