#!/bin/bash

sleep 30
cd /home/pi/program
python wifiReceiver.py &
sleep 1
target_PID="$(pidof -s python wifiReceiver.py)"
nohup python wifiSender.py $target_PID >> /home/pi/Desktop/Data/wifi.txt
