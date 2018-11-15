#!/usr/bin/env bash
export DISPLAY=:0
export NO_AT_BRIDGE=1
cd /home/pi/rotary-club
STATUS=1
#while [ $STATUS -eq 1 ]; do
	/home/pi/rotary-club/main.py
	STATUS=$?
#done
echo $(date) - $STATUS - $(kill -l $STATUS) >> /home/pi/rotary-club/crash.log

