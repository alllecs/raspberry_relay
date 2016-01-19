#!/bin/bash

GPIO=/sys/class/gpio

IO1=5
IO2=6
IO3=13
IO4=19

BUT1=16
BUT2=20
BUT3=21
BUT4=26
BUT5=12

function exp {
	for i in $@; do
		echo $i > $GPIO/export
	done
}

function indirect {
	for i in $@; do
		echo in > $GPIO/gpio$i/direction
	done
}

function highdir {
	for i in $@; do
#		sudo bash -c 'echo high > $GPIO/gpio$i/direction'
		echo high > $GPIO/gpio$i/direction
	done
}
exp $IO1 $IO2 $IO3 $IO4 $BUT1 $BUT2 $BUT3 $BUT4 $BUT5
indirect $BUT1 $BUT2 $BUT3 $BUT4 $BUT5
highdir $IO1 $IO2 $IO3 $IO4
/home/pi/raspberry_relay/i2c/file_simple.py > /dev/null &
