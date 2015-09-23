#!/bin/bash 

BUT1=$1
BUT2=$2
#BUT3=$3
#BUT4=$4
GPIO=/sys/class/gpio

echo $BUT1 > $GPIO/export
echo $BUT2 > $GPIO/export
echo in > $GPIO/gpio$BUT1/direction
echo in > $GPIO/gpio$BUT2/direction
#echo $BUT3 > $GPIO/export
#echo $BUT4 > $GPIO/export

function butt {
	for i in $@; do
		ZN=`tail -n 1 $GPIO/gpio$i/value`

		case $ZN in
		1)
			echo "Кнопка не нажата"
			;;
		0)   
			echo "Кнопка нажата"
			;;
		*)
			echo "Error"
			;;
		esac
	done
}
butt $BUT1 $BUT2
echo $BUT1 > $GPIO/unexport
echo $BUT2 > $GPIO/unexport
