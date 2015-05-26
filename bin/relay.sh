#!/bin/bash

if [ "$1" != "0" -a "$1" != "1" ]; then
        echo "Ошибка ввода"
        exit 1
fi

#echo 04 > /sys/class/gpio/export
#echo out > /sys/class/gpio/gpio4/direction
sudo bash -c "echo $1 > /sys/class/gpio/gpio5/value"
sudo bash -c "echo $1 > /sys/class/gpio/gpio6/value"
sudo bash -c "echo $1 > /sys/class/gpio/gpio13/value"
sudo bash -c "echo $1 > /sys/class/gpio/gpio19/value"
#echo XX > /sys/class/gpio/unexport
