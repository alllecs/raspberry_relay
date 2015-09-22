#!/bin/bash

PORT1=5
PORT2=6
PORT3=13
PORT4=19
GPIO=/sys/class/gpio

function enter {
#	set -x
	echo $1 > $GPIO/export
	echo $2 > $GPIO/gpio$1/direction
	echo $3 > $GPIO/gpio$1/value
#	set +x
}

function init {
	enter $PORT1 out 1 
	enter $PORT2 out 1
	enter $PORT3 out 1
	enter $PORT4 out 1
}

function uninit {
	echo $PORT1 > $GPIO/unexport
	echo $PORT2 > $GPIO/unexport
	echo $PORT3 > $GPIO/unexport
	echo $PORT4 > $GPIO/unexport
}


function res {
	for i in $@; do
		ZN=`tail -n 1 $GPIO/gpio$i/value`
		if [ "$ZN" = "1" ]; then
			echo 0 > $GPIO/gpio$i/value
			sleep 3
			echo 1 > $GPIO/gpio$i/value
		else
			echo 1 > $GPIO/gpio$i/value
			sleep 3
			echo 0 > $GPIO/gpio$i/value
		fi
	done
}

function reset {
       	clear
	echo "Reset"

	options=("Reset 1 Relay" "Reset 2 Relay" "Reset 3 Relay" "Reset 4 Relay" "Reset ALL" "EXIT")
	select on in "${options[@]}"

	do
		case $on in
			"Reset 1 Relay")
				res $PORT1 
				;;
			"Reset 2 Relay")
				res $PORT2
				;;
			"Reset 3 Relay")
				res $PORT3
				;;
			"Reset 4 Relay")
				res $PORT4
				;;
			"Reset ALL")
				res $PORT1 $PORT2 $PORT3 $PORT4
				;;
			"EXIT")
				break
				;;
			 *)
				echo "Make a Selection"
				;;
		esac
	done
}

function pow {
       	clear
	echo "Reset"

	options=("Relay 1" "Relay 2" "Relay 3" "Relay 4" "ALL" "EXIT")
	select on in "${options[@]}"

	do
		case $on in
			"Relay 1")
				onoff $1 $PORT1 
				;;
			"Relay 2")
				onoff $1 $PORT2
				;;
			"Relay 3")
				onoff $1 $PORT3
				;;
			"Relay 4")
				onoff $1 $PORT4
				;;
			"ALL")
				onoff $1 $PORT1
				onoff $1 $PORT2
				onoff $1 $PORT3
				onoff $1 $PORT4
				;;
			"EXIT")
				break
				;;
			 *)
				echo "Make a Selection"
				;;
		esac
	done
}
function onoff {
	echo $1 > $GPIO/gpio$2/value
}

function menu {
	clear

	echo 
	echo -e "\t\tDevice power management\n"
	echo -e "\t1. On"
	echo -e "\t2. Off"
	echo -e "\t3. Reset"
	echo -e "\t4. Information"
	echo -e "\t5. Safety shutdown"
	echo -e "\t0. Exit"
	echo -en "\t\tPlease Make a Selection:"

	read -n 1 option
}

init

while [ $? -ne 1 ]
	do
		menu
		case $option in
		0)
			break
			;;
		1)
			pow 0
			;;
		2)
			pow 1
			;;
		3)
			reset
			;;
		4)
			clear
			echo "web address http://192.168.3.1/admin/index2.html"
			echo "Date: "
			date
			ifconfig eth0
			ifconfig wlan0
			;;
		5)
			onoff 1 $PORT1
			onoff 1 $PORT2
			onoff 1 $PORT3
			onoff 1 $PORT4
				;;
		*)
			clear
			echo "Make a Selection"
			;;
		esac

	echo -en "\n\n\tPress to continue"
	read -n 1 line
	done
#uninit
clear
