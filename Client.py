import socket
import sys
import time

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ('localhost', 5555)

rate_bits_per_sec = 100000000
rate_bytes_per_sec = rate_bits_per_sec/8
lead_seg_id = 0
sleep_time = 0
message = (str(lead_seg_id) + " This is the message.  It will be repeated,")

try:
    sent = sock.sendto(("1"), server_address)
    time.sleep(0.5)
    # For Sending Rate to stabalise
    while True:
        lead_seg_id = 0
        # Sending at 1.5 Mb/s
        while(lead_seg_id < rate_bytes_per_sec + len(message)):
            message = (str(lead_seg_id) + " This is the message.  It will be repeated,")
            sent = sock.sendto((message), server_address)
            lead_seg_id += len(message)
            sleep_time += float(len(message))/rate_bytes_per_sec
            time.sleep(float(len(message))/rate_bytes_per_sec)

finally:
    print ('Closing socket')
    sock.close(
    )

print ('done')
print('done')