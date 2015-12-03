#!/usr/bin/python

import RPi.GPIO as GPIO
import time

STATE_NOTPRESSED = 27
STATE_PRESSED = 28
STATE_ALLREADY = 29

STATE_START = 21
STATE_STAT = 22
STATE_IFACE = 23
STATE_RELAY = 24
STATE_SOCKET = 25
STATE_SHUTDOWN = 26

GPIO.setmode(GPIO.BCM)

class Key:
	def __init__(self, name, gpio):

		self.name = name
		self.gpio = gpio
		self.state = STATE_NOTPRESSED
		GPIO.setup(gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)

	def read_input(self):
		time.sleep(0.01)
		t = GPIO.input(self.gpio)
		if t == False:
			return '0'
		return '1'

	def tick(self):
		key = self.read_input()
		if self.state == STATE_NOTPRESSED:
			if key == '1':
				pass
			elif key == '0':
				self.state = STATE_PRESSED
		elif self.state == STATE_PRESSED:
			if key == '1':
				self.state = STATE_NOTPRESSED
			elif key == '0':
				self.state = STATE_ALLREADY
		elif self.state == STATE_ALLREADY:
			if key == '1':
				self.state = STATE_NOTPRESSED
			elif key == '0':
				pass

	def is_pressed(self):
		if self.state == STATE_PRESSED:
			return True
		return False


class Menu:
	def __init__(self, key1, key2, key3, key4, key5):

		self.key1 = key1
		self.key2 = key2
		self.key3 = key3
		self.key4 = key4
		self.key5 = key5
		self.state = STATE_START
	
	def print_state(self):
		if self.state == STATE_START:
			print("STATE_START");
		elif self.state == STATE_STAT:
			print("STATE_STAT");
		elif self.state == STATE_IFACE:
			print("STATE_IFACE");
		elif self.state == STATE_RELAY:
			print("STATE_RELAY");
		elif self.state == STATE_SOCKET:
			print("STATE_SOCKET");
		elif self.state == STATE_SHUTDOWN:
			print("STATE_SHUTDOWN");
		else:
			print("Warning: Unknown state!");

	def tick(self):
		self.key1.tick()
		self.key2.tick()
		self.key3.tick()
		self.key4.tick()
		self.key5.tick()
		if self.state == STATE_START:
			self.print_state()
			self.state = STATE_STAT
			self.print_state()
		elif self.state == STATE_STAT:
			if self.key1.is_pressed():
				self.state = STATE_SOCKET
				self.print_state()
			elif self.key2.is_pressed():
				self.state = STATE_RELAY
				self.print_state()
			elif self.key3.is_pressed():
				self.state = STATE_IFACE	
				self.print_state()
			elif self.key4.is_pressed():
				self.state = STATE_SHUTDOWN
				self.print_state()
		elif self.state == STATE_SOCKET:
			if self.key1.is_pressed():
				print('socket1 on')
			elif self.key2.is_pressed():
				print('socket1 off')
			elif self.key3.is_pressed():
				print('socket2 on')
			elif self.key4.is_pressed():
				print('socket2 off')
			if self.key5.is_pressed():
				self.state = STATE_STAT
				self.print_state()
		elif self.state == STATE_RELAY:
			if self.key1.is_pressed():
				print('relay1 on')
			elif self.key2.is_pressed():
				print('relay1 off')
			elif self.key3.is_pressed():
				print('relay2 on')
			elif self.key4.is_pressed():
				print('relay2 off')
			if self.key5.is_pressed():
				self.state = STATE_STAT
				self.print_state()
		elif self.state == STATE_IFACE:
			if self.key1.is_pressed():
				print('eth0')
			elif self.key2.is_pressed():
				print('eth1')
			elif self.key3.is_pressed():
				print('wlan0')
			elif self.key4.is_pressed():
				print('wlan1')
			if self.key5.is_pressed():
				self.state = STATE_STAT
				self.print_state()
		elif self.state == STATE_SHUTDOWN:
			if self.key1.is_pressed():
				print('reboot')
			elif self.key2.is_pressed():
				print('halt')
			elif self.key3.is_pressed():
				print('shutdown')
			elif self.key4.is_pressed():
				print('burn')
			if self.key5.is_pressed():
				self.state = STATE_STAT
				self.print_state()
				



key1 = Key("key1", 16)
key2 = Key("key2", 20)
key3 = Key("key3", 21)
key4 = Key("key4", 12)
key5 = Key("key5", 26)

m = Menu(key1, key2, key3, key4, key5)

while True:
	m.tick()
