#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
"""
Clase (y programa principal) para un servidor de eco en UDP simple
"""

import SocketServer
import sys


try:
    IP = sys.argv[1]
    PORT = int(sys.argv[2])
    CANCION = sys.argv[3]
except IndexError:
    print 'Usage: python server.py IP port audio_file'
    raise SystemExit
except ValueError:
    print 'Usage: python server.py IP port audio_file'
    raise SystemExit

metodos = ('INVITE', 'BYE', 'ACK')

class EchoHandler(SocketServer.DatagramRequestHandler):
    """
    SIP Server
    """

    def handle(self):
        print 'Listening...'
        self.wfile.write("Hemos recibido tu peticion\r\n")
        while 1:
            # Leyendo línea a línea lo que nos envía el cliente
            line = self.rfile.read()

            # Si no hay más líneas salimos del bucle infinito
            if not line:
                break            
            print "El cliente nos manda " + line

            #Obtenemos el método del cliente
            metodo = line.split()[0]
            
if __name__ == "__main__":
    # Creamos servidor de eco y escuchamos
    serv = SocketServer.UDPServer(("", PORT), EchoHandler)
    print "Lanzando servidor UDP de eco..."
    serv.serve_forever()
