#!/usr/bin/python
 
import urllib
import cv2
import numpy as np
import os

from skimage import io

os.environ['http_proxy']=''


def afficherImage(lien):
	#url = "http://s0.geograph.org.uk/photos/40/57/405725_b17937da.jpg"
	
	url = lien
	
	url_response = urllib.urlopen(url)
	img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
	img = cv2.imdecode(img_array, -1)
	
	#resize image
	img = cv2.resize(img, None, fx=2.5, fy=2.5, interpolation=cv2.INTER_AREA)
	
	cv2.imshow('Representation 3D', img)
	cv2.waitKey()

