#Веб и текстовый интерфейс управления 4мя реле с помощью raspberry pi

На флешку raspberry pi установлен Raspbian 
c [официального сайта](https://www.raspberrypi.org/downloads/)

проверяем подключение флешки к компьютеру с помощью команды:

  dmesg

и находим строку с нужным /dev/sd?
для каждого она будет своя.

Заливаем на флешку скаченный Raspbian img файл
с помощью команды:

  dd bs=4M if=*-raspbian-wheezy.img of=/dev/sd?

Вставляем подготовленную флешку в raspberri pi.

Подключаемся к raspberry pi по UART.

На ПК заходим под root пользователем.
Командой su.

Подключаемся к rpi и настраиваем по minicom командой:

  minicom -s USB0

Настройте параметры:

  Serial Device : /dev/ttyUSB0
  Bps/Par/Bits : 115200
  Hardware Flow Control : No
  Software Flow Control : No

Для сохранения выберите

  Save setup as USB0

Для выхода нажмите

  Exit

После этого, появится в терминале поле для ввода логина и пароля

Логин: pi
Пароль: raspberry

Далее необходимо зайти под суперпользователем с помощью команды

  sudo bash

Настроить интерфейс в файле /etc/network/interfaces
Открываем командой:

  vi /etc/network/interfaces

Вписываем:

auto eth0
allow-hotplug eth0
iface eth0 inet static
        address 192.168.1.2
        netmask 255.255.255.0
        network 192.168.1.0
        broadcast 192.168.1.255

Для включение ssh сервера выполните команду:

  raspi-config

зайдите в Advanced Options
далее в SSH
нажмите Enable
для выхода нажмите Finish

Подключите raspberry pi к ПК кабелем Ethernet.

Для настройки сети ПК и rpi откройте файл
/etc/network/interfaces на вашем ПК

Добавьте:

auto eth1
allow-hotplug eth1
iface eth1 inet static
        address 192.168.1.1
        netmask 255.255.255.0
        network 192.168.1.0
        broadcast 192.168.0.255

Перезапускаем rpi и отключаем UART.
Теперь есть возможность зайти на rpi по ssh
с помощью команды:

  ssh pi@192.168.1.2

Для подключения rpi к интернету необходимо выполнить проброс
это можно сделать командой на ПК:

  ssh localhost -N -L адрес ПК:порт:прокси:порт

на rpi необходимо выполнить:

  export http_proxy=http://адрес ПК:порт

Для работы веб интерфейса необходимо устновить пакет apache2 b php5
Это можно сделать командой:

  apt-get install apache2 php5 -y

Для работы некоторых команд с веб сайта
необходимо ввести:

  sudo visudo

И в конце добавить строку:

  www-data ALL=(ALL) NOPASSWD: ALL

После настройки rpi появится возможность 
загружать файлы на rpi.

Склонируйте репозиторий на инструментальную ЭВМ
Это можно сделать командой:

git clone https://github.com/alllecs/raspberry_relay.git

Перенос файлов на raspberry pi. По необходимости
создайте отсутствующие каталоги на rasperry pi.

Перенесите файл menu.sh из каталога txt/ в каталог /usr/local/bin/
  scp /txt/menu.sh pi@192.168.1.2:/usr/local/bin/

Перенестие файл relay.sh из каталога bin/  в каталог /var/www/
  scp /bin/relay.sh pi@192.168.1.2:/var/www/

Перенесите файл index.html из каталога web/ в каталог /var/www/
  scp /web/index.html pi@192.168.1.2:/var/www/

Перенестие все файлы кроме index.html из каталога web/
в каталог /var/www/web/ 
  scp /web/* pi@192.168.1.2:/var/www/web/

Для использования веб интерфейса необходимо перейти по ссылке
[RaspberryPi](http://192.168.1.2/)
При необходимости пропишите в прокси браузера:

  192.168.1.2

Для перехода в текстовый интерфейс в командной строке введите команду:

  ssh pi@192.168.1.2

Пароль:

  raspberry

Зайдите под суперпользователем с помощью команды:

  subo bash

Запустите файл menu.sh по адресу /usr/bin/menu.sh командой:

  /usr/bin/menu.sh

В меню выбиреете необходимый вам раздел.

В веб интерфейсе перед работой с реле, необходимо перейти в раздел
"состояние" и нажать на кнопку "export" для нужного реле.

Для замыкания реле, необходимо перейти в раздел питание(power management),
нажать на кнопку "вкл"(power on) соответсвующую нужному реле.

При нажатии на кнопку "выкл"(power off), выбранное реле размыкается.

По окончании работы с реле в веб интерфейсе необходимо
перейти в раздел "состояние" и нажать кнопку "unexport"
для использованных реле.

