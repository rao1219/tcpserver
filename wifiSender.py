import os
import datetime
import subprocess as sub
import time
import sys

def getInterface():
    interfaceList = os.popen('ifconfig | cut -c1-8 | sort -u').read().split('\n')
    
    temp = ''
    information = ''
    interface = ''
    for item in interfaceList:
        item = item.strip()
        if len(item) > 3:
            temp = os.popen('ethtool -i ' + item).read()
            temp = temp.split('\n')
            for info in temp:
                info = info.strip()
                if 'driver' in info and 'usb' in info:
                    interface = item
                    break
    
    monitor = ''
    temp = []
    info = os.popen('sudo airmon-ng start ' + interface).read().split('\n')
    
    for item in info:
        item = item.strip()
        if 'enable' in item:
            temp = item.split(' ')
            monitor = temp[len(temp) - 1].replace(')', '')
            print monitor
            break
    
    if 'wlan1mon' in monitor:
        monitor = 'wlan1mon'

    if 'wlan0mon' in monitor:
        monitor = 'wlan0mon'
    return monitor


def wifiSensing(interfaceName, pid):
    p = sub.Popen(('sudo', 'tcpdump', '-i', interfaceName, '-e', 'type', 'mgt', 'subtype', 'probe-req'), stdout=sub.PIPE)
    path = "myfifo"
    for row in iter(p.stdout.readline, b''):
        data = row.rstrip().split(' ')
        if(data[4] == 'MHz'):
            f = open(path, 'w')
#             result = []
#             result.append(datetime.datetime.now().date().strftime('%m/%d/%Y'))
#             result.append(data[0])
#             result.append(data[12])
#             result.append(data[6])
#             result.append('wifi')
# #             result.append(long)
# #             result.append(lat)
            result = datetime.datetime.now().date().strftime('%m/%d/%Y') + ',' + data[0] + ',' + data[12][3:] + ',' + data[6] + ',' + 'wifi' + ',' + 'na'
            f.write(result + '\n')
            os.kill(pid, 20)
            print result
            f.close()

lat = "nan"
long = "nan"
interface = 'wlan1mon'
pid = int(sys.argv[1])

#sensorID = '1'
monitor = getInterface()
wifiSensing(monitor, pid)
