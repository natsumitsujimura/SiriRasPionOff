#!/usr/bin/python

import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

import cgi

query=cgi.FieldStorage()
switch=query['switch'].value

if switch == "on":
	GPIO.output(21, 1)
elif switch == "off":
	GPIO.output(21, 0)
else:
	GPIO.cleanup()

