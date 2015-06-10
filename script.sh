#!/bin/bash

##Запускать от root.

SD=$1
NAME=2015-05-05-raspbian-wheezy
USER=alecs
set -x

if [ -z "$SD" ]; then
	echo " "
	echo "Введите значение после /dev/ в аргументе"
	fdisk -l
	exit 1
fi

mkdir raspberry
cd raspberry

export http_proxy=http://proxy.cs.niisi.ras.ru:3128
wget http://director.downloads.raspberrypi.org/raspbian/images/raspbian-2015-05-07/${NAME}.zip
unzip ${NAME}.zip

dd bs=8M if=${NAME}.img of=/dev/$SD

fdisk -l
mount /dev/$SD /mnt
cat /home/${USER}/.ssh/id_rsa.pub >> /mnt/home/pi/id_rsa.pub
cp /home/${USER}/.ssh/id_rsa.pub /mnt/.ssh/autorized_keys
cat  www-data ALL=(ALL) NOPASSWD: ALL >> /mnt/etc/sudoers

echo 'Host rpi' >> /home/${USER}/.ssh/config 
echo '	HostName 192.168.1.2' >> /home/${USER}/.ssh/config 
echo '	User root' >> /home/${USER}/.ssh/config


git clone https://github.com/alllecs/raspberry_relay.git

REPO=/home/${USER}/raspberry
scp ${REPO}/txt/menu.sh /mnt/usr/local/bin/

scp ${REPO}/bin/relay.sh /mnt/var/www/

scp ${REPO}/web/index.php /mnt/var/www/

mkdir /mnt/var/www/web
scp ${REPO}/web/*.php /mnt/var/www/web/

umount /dev/sdb2
