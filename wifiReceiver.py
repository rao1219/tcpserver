import os
import signal
import time
import socket

MCAST_GRP = '128.95.204.81'
MCAST_PORT = 9999

def signal_handler(signum, frame):
	data = f.readline()
	while data:
                print(data)
                try:
                        sock.sendto(data.encode(), (MCAST_GRP, MCAST_PORT))
                except:
                        print "failed"
                try:
                        data = f.readline()
                except:
                        print "read failed"

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
path = "myfifo"
if os.path.exists(path) == False:
	os.mkfifo(path)
f = open(path, 'r')
signal.signal(20, signal_handler)

while True:
	time.sleep(10) # save CPU power
f.close() # close file
os.unlink(path) # unlink pipe file
