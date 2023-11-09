#!/usr/bin/env python3
# --------------------------------------------------
# Miguel Riem Oliveira.
# PSR, September 2020.
# Adapted from https://stackabuse.com/basic-socket-programming-in-python/
# -------------------------------------------------
import socket
from dog_lib import Dog
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # create TCP/IP socket
local_hostname = socket.gethostname()  # retrieve local hostname
local_fqdn = socket.getfqdn()  # get fully qualified hostname
ip_address = socket.gethostbyname(local_hostname)  # get the according IP address

server_address = (ip_address, 23456)  # bind the socket to the port 23456, and connect
sock.connect(server_address)
print ("connecting to %s (%s) with %s" % (local_hostname, local_fqdn, ip_address))


dog = Dog('Nono', 'Black', 7)
dog.addBrother('Bobi')
dog.addBrother('Lassie')

print(dog)

# SERIALIZATION -------------------
message = ''
message += dog.name
message += ','
message += dog.color
message += ','
message += str(dog.age)
# ---------------------------------

for brother in dog.brothers:
    message += ','
    message += brother

print('message to send:\n' + str(message))

print ('Sending message: ' + str(message))
message_formatted = str(message).encode("utf-8")
sock.sendall(message_formatted)
time.sleep(2)  # wait for two seconds

sock.close()  # close connection