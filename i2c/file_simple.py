#!/usr/bin/python

import RPi.GPIO as GPIO
import time
import lcddriver
import socket
import fcntl
import struct
import os

STATE_START = 21
STATE_STAT = 22
STATE_IFACE = 23
STATE_RELAY = 24
STATE_SOCKET = 25
STATE_SHUTDOWN = 26
STATE_NOTPRESSED = 27
STATE_PRESSED = 28
STATE_ALLREADY = 29

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
		self.ifname = "eth0"

		self.up = None
		self.down = None
		self.enter = None
		self.esc = None
	
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

	def get_ip_address(self, ifname):
	    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	    return socket.inet_ntoa(fcntl.ioctl(
	        s.fileno(),
	        0x8915,  # SIOCGIFADDR
	        struct.pack('256s', ifname[:15])
	    )[20:24])

	def newfunc(self, gpionum):
	        f1 = open('/sys/class/gpio/gpio%d/value' % gpionum)
	        A = f1.readline(1)
	        if A == "1":
	                return "Off"
	        else:
	                return "On "
	
	def display_stat(self):
        	lcd.lcd_clear()
		date_str = time.strftime("%Y %b %d %H:%M")
	        lcd.lcd_display_string("Socket 1:" + self.newfunc(5) + ", 2:" + self.newfunc(6), 1)
	        lcd.lcd_display_string("Relay 1:" + self.newfunc(13) + ", 2:" + self.newfunc(19), 2)
	        lcd.lcd_display_string(date_str, 3)
	        lcd.lcd_display_string("IP: " + self.get_ip_address('eth0'), 4)

	def menu2_init(self, up, down, enter, esc):
		self.up = up
		self.down = down
		self.enter = enter
		self.esc = esc

	def menu2(self, l1, l2, l3, l4):
        	lcd.lcd_clear()
		lcd.lcd_display_string("  " + l1, 1)
		lcd.lcd_display_string("  " + l2, 2)
		lcd.lcd_display_string("  " + l3, 3)
		lcd.lcd_display_string("  " + l4, 4)
		last_keypressed = time.time()	
		selected = 1
		while True:
			cur_time = time.time()
			self.up.tick()
			self.down.tick()
			self.enter.tick()
			self.esc.tick()
			lcd.lcd_display_string("> ", selected)
			if self.up.is_pressed():
				lcd.lcd_display_string("  ", selected)
				selected = selected - 1
				if selected < 1:
					selected = 4
			elif self.down.is_pressed():
				lcd.lcd_display_string("  ", selected)
				selected = selected + 1
				if selected > 4:
					selected = 1
			elif self.enter.is_pressed():
				return selected
			elif self.esc.is_pressed() or cur_time - last_keypressed > 20:
				return 5

	def tick(self):
		self.key1.tick()
		self.key2.tick()
		self.key3.tick()
		self.key4.tick()
		self.key5.tick()
		if self.state == STATE_START:
#			start_time = time.time()
			if self.key1.is_pressed() or self.key2.is_pressed() or self.key3.is_pressed() or self.key4.is_pressed() or self.key5.is_pressed():
				self.print_state()
#				menu_time = time.time() 
				self.state = STATE_STAT
				self.print_state()
#			elif start_time - menu_time > 30:
#				self.display_stat()
		elif self.state == STATE_STAT:
			self.menu2_init(self.key1, self.key2, self.key3, self.key4)
			rc = self.menu2("Socket", "Relay", "Interface", "Shutdown")
			if rc == 1:
				self.state = STATE_SOCKET
				self.print_state()
			elif rc == 2:
				self.state = STATE_RELAY
				self.print_state()
			elif rc == 3:
				self.state = STATE_IFACE	
				self.print_state()
			elif rc == 4:
				self.state = STATE_SHUTDOWN
				self.print_state()
			elif rc == 5:
				self.state = STATE_START
				self.display_stat()
		elif self.state == STATE_SOCKET:
			rc = self.menu2("Socket 1 on", "Socket 1 off", "Socket 2 on", "Socket 2 off")
			if rc == 1:
				print('socket1 on')
				os.system("echo 0 > /sys/class/gpio/gpio5/value")
			elif rc == 2:
				print('socket1 off')
				os.system("echo 1 > /sys/class/gpio/gpio5/value")
			elif rc == 3:
				print('socket2 on')
				os.system("echo 0 > /sys/class/gpio/gpio6/value")
			elif rc == 4:
				print('socket2 off')
				os.system("echo 1 > /sys/class/gpio/gpio6/value")
			elif rc == 5:
				self.state = STATE_STAT
				self.print_state()
		elif self.state == STATE_RELAY:
			rc = self.menu2("Relay 1 on", "Relay 1 off", "Relay 2 on", "Relay 2 off")
			if rc == 1:
				print('relay1 on')
				os.system("echo 0 > /sys/class/gpio/gpio13/value")
			elif rc == 2:
				print('relay1 off')
				os.system("echo 1 > /sys/class/gpio/gpio13/value")
			elif rc == 3:
				print('relay2 on')
				os.system("echo 0 > /sys/class/gpio/gpio19/value")
			elif rc == 4:
				print('relay2 off')
				os.system("echo 1 > /sys/class/gpio/gpio19/value")
			if rc == 5:
				self.state = STATE_STAT
				self.print_state()
		elif self.state == STATE_IFACE:
			rc = self.menu2("eth0", "eth1", "wlan0", "localhost")
			if rc == 1:
				print('eth0')
				lcd.lcd_display_string(self.get_ip_address('eth0'), 1)
				time.sleep(3)
			elif rc == 2:
				print('eth1')
				lcd.lcd_display_string(self.get_ip_address('eth1'), 1)
			elif rc == 3:
				print('wlan0')
				lcd.lcd_display_string(self.get_ip_address('wlan0'), 1)
			elif rc == 4:
				print('localhost')
			elif rc == 5:
				self.state = STATE_STAT
				self.print_state()
		elif self.state == STATE_SHUTDOWN:
			rc = self.menu2("Reboot", "Halt", "Shutdown", "Burn")
			if rc == 1:
				os.system("reboot")
				print('reboot')
			elif rc == 2:
				print('halt')
				os.system("halt")
			elif rc == 3:
				print('shutdown')
				os.system("shutdown -h now")
			elif rc == 4:
				print('burn')
			elif rc == 5:
				self.state = STATE_STAT
				self.print_state()

key1 = Key("key1", 16)
key2 = Key("key2", 20)
key3 = Key("key3", 21)
key4 = Key("key4", 12)
key5 = Key("key5", 26)
lcd = lcddriver.lcd()
lcd.lcd_clear()

m = Menu(key1, key2, key3, key4, key5)

while True:
	m.tick()
