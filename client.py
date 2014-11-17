#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Programa cliente que abre un socket a un servidor
"""

import socket
import sys

# Cliente UDP simple.

#Comprobamos errores en los datos
metodos = ('INVITE', 'BYE')

try:
    METODO = sys.argv[1]
    USER = sys.argv[2].split('@')[0]
    IP = sys.argv[2].split('@')[1].split(':')[0]
    PORT = int(sys.argv[2].split(':')[1])
    if not METODO in metodos:
        print 'Usage: python client.py method receiver@IP:SIPport'
        raise SystemExit
except IndexError:
    print 'Usage: python client.py method receiver@IP:SIPport'
    raise SystemExit
except ValueError:
    print 'Usage: python client.py method receiver@IP:SIPport'
    raise SystemExit


# Contenido que vamos a enviar
LINE = '¡Hola mundo!'

# Creamos el socket, lo configuramos y lo atamos a un servidor/puerto
my_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
my_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
my_socket.connect((IP, PORT))

print "Enviando: " + LINE
my_socket.send(LINE + '\r\n')

#Comprobamos que se escucha en el servidor
try:
    data = my_socket.recv(1024)
except socket.error:
    print 'Error: No server listening at ' + IP + ' port ' + str(PORT)
    raise SystemExit

print 'Recibido -- ', data
print "Terminando socket..."

# Cerramos todo
my_socket.close()
print "Fin."
