import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('localhost', 5555)
print >> sys.stderr, 'starting up on %s port %s' % server_address
print('\nWaiting to receive message...')
sock.bind(server_address)
total_received_bytes = 0

while True:
    data, address = sock.recvfrom(4096)
    if len(data) == 1:
        timestamp = time.time()
        break

# Sleep else there will be float divison by zero error
time.sleep(0.5)

while True:
    data, address = sock.recvfrom(4096)

    donestamp = time.time()
    data = len(data)
    total_received_bytes += data

    rate = (total_received_bytes / (donestamp - timestamp))
    print "\nRcvd: %s bytes, %s total in %s s at %s bytes per second" % (data, total_received_bytes, donestamp - timestamp, rate)


    
