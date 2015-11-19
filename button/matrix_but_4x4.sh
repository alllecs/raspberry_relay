#!/bin/bash

BUT0=18
BUT1=23
BUT2=24
BUT3=25
BUT4=12
BUT5=16
BUT6=20
BUT7=21
GPIO=/sys/class/gpio

function exp {
	for i in $@; do
		echo $i > $GPIO/export
	done
}

function unexp {
	for i in $@; do
		echo $i > $GPIO/unexport
	done
}

function gpin {
	for i in $@; do
		echo in > $GPIO/gpio$i/direction
	done
}

function gpout {
	for i in $@; do
		echo out > $GPIO/gpio$i/direction
		echo 1 > $GPIO/gpio$i/value
	done
}
function powon {
	for i in $@; do
		echo 0 > $GPIO/gpio$i/value
	done
}

function powoff {
	for i in $@; do
		echo 1 > $GPIO/gpio$i/value
	done
}

function stat {
	for i in $@; do
		ZN=`tail -n 1 $GPIO/gpio$i/value`

		case $ZN in
		1)
			echo "не нажата"
			;;
		0)
			echo "нажата"
			;;
		*)
			echo "ERROR"
			;;
		esac
	done
}

exp $BUT0 $BUT1 $BUT2 $BUT3 $BUT4 $BUT5 $BUT6 $BUT7
gpout $BUT0 $BUT1 $BUT2 $BUT3
gpin $BUT4 $BUT5 $BUT6 $BUT7

i=0
while [ $i -lt 4 ]; do
	var1="BUT$i"
	ADDR=${GPIO}/gpio${!var1}/value
	echo 0 > ${ADDR}
	j=4
	while [ $j -lt 8 ]; do
		var2="BUT$j"
		ADDR1=${GPIO}/gpio${!var2}/value
		ZN=`tail -n 1 ${GPIO}/gpio${!var2}/value`
		if [ $ZN -eq 0 ]; then
			NUM=$[$i*4+$j-3]
			echo "Кнопка $NUM нажата"
		fi
		j=$[$j+1]
		done
	echo 1 > ${ADDR}
	i=$[$i+1]
	done

unexp $BUT0 $BUT1 $BUT2 $BUT3 $BUT4 $BUT5 $BUT6 $BUT7
