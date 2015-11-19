#!/bin/bash 

BUT1=16
BUT2=20
BUT3=21
BUT4=26
BUT5=12
J=0
IO1=5
IO2=6
IO3=13
IO4=19
GPIO=/sys/class/gpio

function offall {
	i=$1
	ZN=`tail -n 1 $GPIO/gpio$i/value`

	case $ZN in
	0)
		;;
	1)
		echo 1 > $GPIO/gpio$2/value
		echo 1 > $GPIO/gpio$3/value
		echo 1 > $GPIO/gpio$4/value
		echo 1 > $GPIO/gpio$5/value
		;;
	*)
		echo "Error"
		;;
	esac
}

function butt {
#	for i in $@; do
	i=$1
	n=$2
		ZN=`tail -n 1 $GPIO/gpio$i/value`

		case $ZN in
		0)
#			echo "Кнопка не нажата"
			;;
		1)   
#			echo "Кнопка нажата"
			power $n
			python i2c/file.py
			;;
		*)
			echo "Error"
			;;
		esac
#	done
}

function power {
	for i in $@; do
		ZN=`tail -n 1 $GPIO/gpio$i/value`

		case $ZN in
		1)
			echo 0 > $GPIO/gpio$i/value
			;;
		0)   
			echo 1 > $GPIO/gpio$i/value
			;;
		*)
			echo "Error"
			;;
		esac
	done
}
while [ $J -lt 60 ]
do 
	butt $BUT1 $IO1
	butt $BUT2 $IO2
	butt $BUT3 $IO3
	butt $BUT4 $IO4
	offall $BUT5 $IO1 $IO2 $IO3 $IO4
	sleep 1
	let J=J+1
done
