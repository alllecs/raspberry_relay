#!/usr/bin/python
import RPi.GPIO as GPIO
import time

STATE_START = 21
STATE_STAT = 22
STATE_IFACE = 23
STATE_RELAY = 24
STATE_SOCKET = 25
STATE_SHUTDOWN = 26

GPIO.setmode(GPIO.BCM)
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(20, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def read_input():
	key = ""
	while key not in ('1', '2', '3', '4', '5'):
#		key = raw_input("Key?")
		state1 = GPIO.input(16)
		time.sleep(0.1)
		state2 = GPIO.input(20)
		time.sleep(0.1)
		state3 = GPIO.input(21)
		time.sleep(0.1)
		state4 = GPIO.input(12)
		time.sleep(0.1)
		state5 = GPIO.input(26)
		time.sleep(0.1)

		if state1 == False:
			key = '1'
		elif state2 == False:
			key = '2'
		elif state3 == False:
			key = '3'
		elif state4 == False:
			key = '4'
		elif state5 == False:
			key = '5'
	return key

def print_state(state):
	if state == STATE_START:
		print("STATE_START");
	elif state == STATE_STAT:
		print("STATE_STAT");
	elif state == STATE_IFACE:
		print("STATE_IFACE");
	elif state == STATE_RELAY:
		print("STATE_RELAY");
	elif state == STATE_SOCKET:
		print("STATE_SOCKET");
	elif state == STATE_SHUTDOWN:
		print("STATE_SHUTDOWN");
	else:
		print("Warning: Unknown state!");

state = STATE_START

while True:
	print_state(state)
	if state == STATE_START:
		state = STATE_STAT
		continue
	elif state == STATE_STAT:
		key = read_input()
		if key == '1':
			state = STATE_SOCKET	
		if key == '2':
			state = STATE_RELAY
		if key == '3':
			state = STATE_IFACE	
		if key == '4':
			state = STATE_SHUTDOWN
		continue
	elif state == STATE_SOCKET:
		key = read_input()
		if key == '5':
			state = STATE_STAT	
		continue
	elif state == STATE_RELAY:
		key = read_input()
		if key == '5':
			state = STATE_STAT
		continue
	elif state == STATE_IFACE:
		key = read_input()
		if key == '5':
			state = STATE_STAT
		continue
	elif state == STATE_SHUTDOWN:
		key = read_input()
		if key == '5':
			state = STATE_STAT
		continue
