#!/bin/bash

sleep 30
cd /home/pi/program
python blueReceiver.py &
sleep 1
target_PID="$(pidof -s python blueReceiver.py)"
nohup python blueSender.py $target_PID >> /home/pi/Desktop/Data/bluetooth.txt
