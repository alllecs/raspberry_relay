#Веб и текстовый интерфейс управления 4 реле с помощью Raspberry Pi

На SD карту Raspberry Pi(rpi) установливаем Raspbian 
c [официального сайта](https://www.raspberrypi.org/downloads/).

Проверяем подключение SD карты к ПК с помощью команды:
````
  dmesg
````
и находим строку с нужным /dev/sd?
для каждого она будет своя.

Заливаем на SD карту, скаченный Raspbian img файл,
с помощью команды:
````
  dd bs=4M if=*-raspbian-wheezy.img of=/dev/sd?
````
Вставляем подготовленную флешку в rpi.

Подключаемся к rpi по UART.
Для этого:

На ПК заходим под root пользователем.
Командой su.

Подключаемся к rpi и настраиваем minicom командой:
````
  minicom -s USB0
````
Настройте параметры:
````
  Serial Device : /dev/ttyUSB0
  Bps/Par/Bits : 115200
  Hardware Flow Control : No
  Software Flow Control : No
````
Для сохранения выберите
````
  Save setup as USB0
````
Для выхода нажмите
````
  Exit
````
После этого, появится в терминале поле для ввода логина и пароля
````
  Логин: pi
  Пароль: raspberry
````
Далее необходимо зайти под суперпользователем на rpi,
с помощью команды:
````
  sudo bash
````
Настроить интерфейс rpi в файле /etc/network/interfaces
Открываем командой:
````
  vi /etc/network/interfaces
````
Добавить или заменить:

````
auto eth0
allow-hotplug eth0
iface eth0 inet static
        address 192.168.1.2
        netmask 255.255.255.0
        network 192.168.1.0
        broadcast 192.168.1.255
````
Перезапустить rpi.


Для включение ssh сервера на rpi выполните команду:
````
  raspi-config
````
зайдите в Advanced Options
далее в SSH
нажмите Enable
для выхода нажмите Finish

Подключите rpi к ПК по интерфейсу Ethernet.

Для настройки соединения ПК и rpi откройте файл
/etc/network/interfaces на вашем ПК

Добавьте:
````
auto eth1
allow-hotplug eth1
iface eth1 inet static
        address 192.168.1.1
        netmask 255.255.255.0
        network 192.168.1.0
        broadcast 192.168.0.255
````
Перезапускаем rpi и отключаем UART.
Теперь есть возможность зайти на rpi по ssh
с помощью команды:
````
  ssh pi@192.168.1.2
````
Для подключения rpi к интернету необходимо выполнить тунель
это можно сделать командой на ПК:
````
  ssh localhost -N -L ip_адрес_ПК:порт:прокси:порт
````
на rpi выполнить:
````
  export http_proxy=http://ip_адрес_ПК:порт
````
Для работы веб интерфейса на rpi необходимо устновить пакет apache2 и php5
Это можно сделать командой:
````
  apt-get install apache2 php5 -y
````
Для работы некоторых команд выполняющихся по веб интерфейсу
необходимо ввести:
````
  sudo visudo
````
И в конце добавить строку:
````
  www-data ALL=(ALL) NOPASSWD: ALL
````
После настройки rpi появится возможность 
загружать файлы на rpi.

Склонируйте репозиторий на инструментальную ЭВМ
Это можно сделать командой:
````
  git clone https://github.com/alllecs/raspberry_relay.git
````
Перенос файлов на raspberry pi. По необходимости
создайте отсутствующие каталоги на rasperry pi.

Для удобства подключения и переноса файлов на rpi 
скопируйте файл .ssh/id_rsa.pub со своего ПК
на raspberry pi в файл .ssh/authorized_keys
с помощью команд:
````
  scp .ssh/id_rsa.pub pi@192.168.1.2:

  Пароль: raspberry

  ssh pi@192.168.1.2
  Пароль: raspberry

  sudo bash
  cp ~pi/id_rsa.pub ~/.ssh/authorized_keys
````
Добавьте в файл на своем ПК .ssh/config:
````
  Host rpi
    HostName 192.168.1.2
    User root
````
После чего можно подключаться к raspberry pi командой:
````
  ssh rpi
````
В дальнейшем изложении переменная REPO хранит путь к репозиторию: 
/home/user/raspberry/

Перенесите файл menu.sh из каталога txt/ в каталог /usr/local/bin/
````
  scp ${REPO}/txt/menu.sh rpi:/usr/local/bin/
````
Перенесите файл relay.sh из каталога bin/  в каталог /var/www/
````
  scp ${REPO}/bin/relay.sh rpi:/var/www/
````
Перенесите файл index.php из каталога web/ в каталог /var/www/
````
  scp ${REPO}/web/index.php rpi:/var/www/
````
Перенесите все файлы кроме index.php из каталога web/
в каталог /var/www/web/ 
````
  scp ${REPO}/web/*.php rpi:/var/www/web/
````
Для использования веб интерфейса необходимо перейти по ссылке
[RaspberryPi](http://192.168.1.2/)
По необходимости запретите в браузере доступк к rpi:
````
  192.168.1.2
````
Для перехода в текстовый интерфейс в командной строке введите команду:
````
  ssh rpi
````
Пароль:
````
  raspberry
````
Запустите файл menu.sh по адресу /usr/local/bin/menu.sh командой:
````
  /usr/local/bin/menu.sh
````
В меню выберите необходимый вам раздел.

В веб интерфейсе перед работой с реле, необходимо перейти в раздел
"состояние" и нажать на кнопку "export" для нужного реле.

Для замыкания реле, необходимо перейти в раздел питание(power management),
нажать на кнопку "вкл"(power on) соответсвующую нужному реле.

При нажатии на кнопку "выкл"(power off), выбранное реле размыкается.

По окончании работы с реле в веб интерфейсе необходимо
перейти в раздел "состояние" и нажать кнопку "unexport"
для использованных реле.

