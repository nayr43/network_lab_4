import socket
import sys
import time

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to the port
server_address = ('10.0.0.1', 5555)
print >> sys.stderr, 'starting up on %s port %s' % server_address
print('\nWaiting to receive message...')
sock.bind(server_address)
total_received_bytes = 0
prev_lead_seg_id = 0
missing_packets = []

while True:
    data, address = sock.recvfrom(4096)
    lead_seg_id = int(data.split()[0])
    print(lead_seg_id)
    prev_lead_seg_id+=1
    if (lead_seg_id != prev_lead_seg_id):
        if (lead_seg_id in missing_packets):
            missing_packets.remove(lead_seg_id)
        else:
            missing_packets.append(prev_lead_seg_id)
        if (len(missing_packets) > 0):
            if (missing_packets[0] < lead_seg_id - 10):
                print('Warning: Packet #%d has been dropped.' %(missing_packets[0]) )
                missing_packets.remove(missing_packets[0])

    # donestamp = time.time()
    # data = len(data)
    # total_received_bytes += data
    #
    # rate = (total_received_bytes / (donestamp - timestamp))
    # print "\nRcvd: %s bytes, %s total in %s s at %s bytes per second" % (data, total_received_bytes, donestamp - timestamp, rate)
