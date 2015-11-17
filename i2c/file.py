#!/usr/bin/env python
import RPi.GPIO as GPIO
import lcddriver
import socket
import fcntl
import struct
import time

#from time import *

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])

lcd = lcddriver.lcd()

lcd.lcd_clear()

def newfunc(gpionum):
	f1 = open('/sys/class/gpio/gpio%d/value' % gpionum)
	A = f1.readline(1)
	if A == "1":
		return "Off"
	else:
		return "On "

lcd.lcd_display_string("Socket 1:" + newfunc(5) + ", 2:" + newfunc(6), 1)
lcd.lcd_display_string("Relay 1:" + newfunc(13) + ", 2:" + newfunc(19), 2)

date_str = time.strftime("%Y %b %d %H:%M")

lcd.lcd_display_string(date_str, 3)
lcd.lcd_display_string("IP: " + get_ip_address('eth0'), 4)
