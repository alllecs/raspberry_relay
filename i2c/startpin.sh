#!/bin/bash

echo 5 > /sys/class/gpio/export
echo 6 > /sys/class/gpio/export
echo 13 > /sys/class/gpio/export
echo 19 > /sys/class/gpio/export

sudo bash -c 'echo high > /sys/class/gpio/gpio5/direction'
sudo bash -c 'echo high > /sys/class/gpio/gpio6/direction'
sudo bash -c 'echo high > /sys/class/gpio/gpio13/direction'
sudo bash -c 'echo high > /sys/class/gpio/gpio19/direction'
