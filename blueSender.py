'''
Created on Dec 24, 2016

@author: Ziyuan Pu
'''
import os
import datetime
import subprocess as sub
import time
import sys

def blueInter():
    interfaceList = info = os.popen('hciconfig').read().split('\n')
    if len(interfaceList) > 6:
        for item in interfaceList:
            if 'hci' in item:
                item = item.split(':')
                interface = ''
                for element in item:
                    element = element.strip()
                    if 'hci' in element:
#                         print element                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
                        interface = element
                    
                    if 'UART' in element:
#                         print element
                        os.system('sudo hciconfig ' + interface + ' down')
                    
                    if 'USB' in element:
#                         print element
                        os.system('sudo hciconfig ' + interface + ' up')

def bluetooth(pid):
    while True:
        #     os.system("hcitool scan")
            dev = sub.Popen(["hcitool scan"], stdout=sub.PIPE, shell=True)
            (device, err) = dev.communicate()
            device = device.replace("Scanning ..."+ "\n", "")
            device = device.split("\n")
            path = "myfifo2"
            for item in device:
                if(item != ""):
                    f = open(path, 'w')
                    mac = item.split()
                    result = time.strftime("%m/%d/%Y") + ',' + time.strftime("%H:%M:%S") + ',' + mac[0] + ',' + '0' +  ',' + "bluetooth" + ',' + str(mac[1:])
                    f.write(result + '\n')
                    os.kill(pid, 20)
                    print result
                    f.close()


lat = "nan"
long = "nan"
pid = int(sys.argv[1])

#sensorID = '1'
blueInter()
bluetooth(pid)

