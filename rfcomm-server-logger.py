# file: rfcomm-server.py
# auth: Albert Huang <albert@csail.mit.edu>
# desc: simple demonstration of a server application that uses RFCOMM sockets
#
# $Id: rfcomm-server.py 518 2007-08-10 07:20:07Z albert $

from subprocess import call
call(["/usr/bin/sdptool", "add", "SP"])

import sys
sys.path.append('/home/pi/hom/')

from bluetooth import *
from filebeep import filebeep

log = open('/home/pi/hom/rfcomm.log', 'w')
print >>log, "Arquivo criado"
log.close()

def loga(comando):
    log = open('/home/pi/hom/rfcomm.log', 'a')
    print >>log, comando
    log.close()

server_sock=BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

loga("socket criado") 

port = server_sock.getsockname()[1]

loga("Criado canal {0}".format(str(port)))

uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

advertise_service( server_sock, "SampleServer",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ], 
#                   protocols = [ OBEX_UUID ] 
                    )


loga("Waiting for connection on RFCOMM channel {0}".format(str(port)))
client_sock, client_info = server_sock.accept()
loga("Accepted connection from {0}".format(str(client_info)))

try:
    while True:
        data = client_sock.recv(1024)
        if len(data) == 0: break
        loga("received [{0}]".format(str(data)))
        if data == 'tocaRaul':
            filebeep()
        if data == 'oi':
            client_sock.send("Hello World")
except IOError:
    pass

loga("disconnected")

client_sock.close()
server_sock.close()

loga("all done")
