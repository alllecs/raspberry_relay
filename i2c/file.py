#!/usr/bin/env python
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
	# "gpio%d/value" % (gpionum,)
	if f1:

	return f1.readline(1)

#f1 = open('/sys/class/gpio/gpio5/value')
f2 = open('/sys/class/gpio/gpio6/value')
f3 = open('/sys/class/gpio/gpio13/value')
f4 = open('/sys/class/gpio/gpio19/value')

lcd.lcd_display_string("Relay 1:" + newfunc(5) + " Relay 2:" + f2.readline(1), 1)
lcd.lcd_display_string("Relay 3:" + f3.readline(1) + " Relay 4:" + f4.readline(1), 2)

date_str = time.strftime("%Y %b %d %H:%M")

lcd.lcd_display_string(date_str, 3)
lcd.lcd_display_string("IP: " + get_ip_address('eth0'), 4)
