#!/usr/bin/python

# la partie cachee est pour la version 2.7 de python
#import BaseHTTPServer
#import CGIHTTPServer


#PORT = 8888
#server_address = ("localhost", PORT)

#server = BaseHTTPServer.HTTPServer
#handler = CGIHTTPServer.CGIHTTPRequestHandler
#handler.cgi_directories = ["/mycgi]
#print ("Serveur actif sur le port :", PORT)

#httpd = server(server_address, handler)
#httpd.serve_forever()

# cette partie du code est pour python 3
import http.server

PORT = 8000
class Handler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ["/server"]

print ("Serveur actif sur le port :", PORT)
server = http.server.HTTPServer(("192.168.43.93", PORT),Handler)
server.serve_forever()
