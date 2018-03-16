#!/usr/bin/python
 
import httplib
import urllib
import json

from afficher import *

#API with bin packing

#,{"w": 3, "h": 3, "d": 3, "q": 3, "vr": 1, "wg": 0, "id": "Item2"}
#{"w": 5, "h": 5, "d": 1, "q": 2, "vr": 1, "wg": 0, "id": "Item1"},
#,{"w": 2, "h": 8, "d": 8, "q": 1, "vr": 0, "wg": 0, "id": "Item3"}
def solveur3D (conteneur = [], datas = []):
	conn = httplib.HTTPConnection(host='eu.api.3dbinpacking.com', port=80)
	
	if datas == [] and conteneur == []:
		data = {"bins": [{"w": 10, "h": 10, "d": 10, "max_wg": 1000, "id": "Bin1"}], "items": [{"w": 3, "h": 3, "d": 3, "q": 9, "vr": 1, "wg": 5, "id": "Item2"},{"w": 2, "h": 8, "d": 8, "q": 1, "vr": 1, "wg": 200, "id": "Item3"}], "username": "parisantoi", "api_key": "f99177be0ff90ae0263f9154f79ffab3", "params": {"images_background_color": "255,255,255", "images_bin_border_color": "59,59,59", "images_bin_fill_color": "230,230,230", "images_item_border_color": "214,79,79", "images_item_fill_color": "177,14,14", "images_item_back_border_color": "215,103,103", "images_sbs_last_item_fill_color": "99,93,93", "images_sbs_last_item_border_color": "145,133,133", "images_width": 100, "images_height": 100, "images_source": "file", "images_sbs": 1, "stats": 1, "item_coordinates": 1, "images_complete": 1, "images_separated": 1}}
	elif datas != [] and conteneur != [] :
		data = {"bins": conteneur, "items": datas, "username": "parisantoi", "api_key": "f99177be0ff90ae0263f9154f79ffab3", "params": {"images_background_color": "255,255,255", "images_bin_border_color": "59,59,59", "images_bin_fill_color": "230,230,230", "images_item_border_color": "214,79,79", "images_item_fill_color": "177,14,14", "images_item_back_border_color": "215,103,103", "images_sbs_last_item_fill_color": "99,93,93", "images_sbs_last_item_border_color": "145,133,133", "images_width": 100, "images_height": 100, "images_source": "file", "images_sbs": 1, "stats": 1, "item_coordinates": 1, "images_complete": 1, "images_separated": 1}}
	else :
		print "probleme dans transmission de donnees !!"
		return
	 
	params =  urllib.urlencode( {'query':json.dumps(data)} )
	headers = {"Content-type": "application/x-www-form-urlencoded",
		"Accept": "text/plain"}
	conn.request( "POST", "/packer/pack", params, headers )
	content = conn.getresponse( ).read( )
	conn.close( )

	d = json.loads(content)
	
	timeExec = d["response"]["response_time"]
	print "Temps exec -> {}s".format(timeExec)
	"""
	not_packed_items = d["response"]["not_packed_items"]
	
	
	print "liste des objets non places ({}) : ".format(len(not_packed_items))
	if len(not_packed_items) > 0:
		for o in not_packed_items:
			print o
	"""
	d1 = d["response"]["bins_packed"][0]
	#print d1
	#print d1["items"].keys()
	d2 = d1["items"]
	nbItem = len(d2)
	#print nbItem
	#print len(datas)

	print "Nombre d'objets places : {} / {}".format(nbItem, len(datas))
	
	for k in d2:
		print "{} -> ({}, {}, {}) - ({}, {}, {})".format(k["id"], k["coordinates"]["x1"], k["coordinates"]["y1"], k["coordinates"]["z1"], k["coordinates"]["x2"], k["coordinates"]["y2"], k["coordinates"]["z2"])
		
	
	lastImage = d2[(nbItem-1)]["image_sbs"]
	#print(lastImage)

	afficherImage (lastImage)
	
def solveurLevel3D (conteneur = [], datas = []):
	conn = httplib.HTTPConnection(host='eu.api.3dbinpacking.com', port=80)
	
	if datas != [] and conteneur != [] :
		data = {"bins": conteneur, "items": datas, "username": "parisantoi", "api_key": "f99177be0ff90ae0263f9154f79ffab3", "params": {"images_background_color": "255,255,255", "images_bin_border_color": "59,59,59", "images_bin_fill_color": "230,230,230", "images_item_border_color": "214,79,79", "images_item_fill_color": "177,14,14", "images_item_back_border_color": "215,103,103", "images_sbs_last_item_fill_color": "99,93,93", "images_sbs_last_item_border_color": "145,133,133", "images_width": 100, "images_height": 100, "images_source": "file", "images_sbs": 1, "stats": 1, "item_coordinates": 1, "images_complete": 1, "images_separated": 1}}
	else :
		print "probleme dans transmission de donnees !!"
		return
	 
	params =  urllib.urlencode( {'query':json.dumps(data)} )
	headers = {"Content-type": "application/x-www-form-urlencoded",
		"Accept": "text/plain"}
	conn.request( "POST", "/packer/pack", params, headers )
	content = conn.getresponse( ).read( )
	conn.close( )

	d = json.loads(content)

	d1 = d["response"]["bins_packed"][0]
	d2 = d1["items"]
	
	return d2
		
		
		

	
#Autre API
def test():
	conn = httplib.HTTPConnection(host='www.packit4me.com', port=80)
	params =  urllib.urlencode({'bins': '0:50:5x5x5', 'items': '0:0:5:1x2x3,1:0:10:2x4x2'})
	headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
	conn.request("POST", "/api/call/raw", params, headers)
	content = conn.getresponse().read()
	conn.close()

	print content
	
