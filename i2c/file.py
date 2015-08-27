#!/usr/bin/env python
import lcddriver
from time import *

lcd = lcddriver.lcd()

lcd.lcd_clear()
lcd.lcd_display_string("  IP: 192.168.1.2", 4)
lcd.lcd_display_string("--------------------", 3)

f1 = open('/sys/class/gpio/gpio5/value')
f2 = open('/sys/class/gpio/gpio6/value')
f3 = open('/sys/class/gpio/gpio13/value')
f4 = open('/sys/class/gpio/gpio19/value')

lcd.lcd_display_string("Relay 1: " + f1.readline(1) + " Relay 2:" + f2.readline(
1), 1)
lcd.lcd_display_string("Relay 3: " + f3.readline(1) + " Relay 4:" + f4.readline(
1), 2)

