import os
import signal
import time
import socket
import threading
import time

#MCAST_GRP = '128.95.204.81'
MCAST_GRP = '127.0.0.1'
MCAST_PORT = 9999
#
#def signal_handler(signum, frame):
#	data = f.readline()
#	while data:
#                print(data)
#                try:
#                        sock.sendto(data.encode(), (MCAST_GRP, MCAST_PORT))
#                except:
#                        print "failed"
#                try:
#                        data = f.readline()
#                except:
#                        print "read failed"
#
#sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
#sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_TTL, 2)
#path = "myfifo"
#if os.path.exists(path) == False:
#	os.mkfifo(path)
#f = open(path, 'r')
#signal.signal(20, signal_handler)
#
#while True:
#	time.sleep(10) # save CPU power
#f.close() # close file
#os.unlink(path) # unlink pipe file

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((MCAST_GRP, MCAST_PORT))
s.listen(5)
print('Waiting for connection...')


def tcplink(sock, addr):
    print('Accept new connection from %s:%s...' % addr)
    sock.send(b'Welcome!')
    while True:
        time.sleep(1)
        data = sock.recv(1024)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello, %s!' % data.decode('utf-8')).encode('utf-8'))
    sock.close()
    print('Connection from %s:%s closed.' % addr)


while True:
    sock, addr = s.accept()
    # print('sock = %s, addr = %s' % (sock, addr))
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
