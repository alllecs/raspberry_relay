<html>
	<head>
		<meta charset=utf-8" />
		<style>
                table {
                        width: 1000px; /* Ширина таблицы */
			border: 1px solid silver;
                        margin: auto; /* Выравниваем таблицу по центру окна  */
                }
                td {
                        text-align: center; /* Выравниваем текст по центру ячейки */
		}
					
                </style>


	</head>

	<body bgcolor="#F5F5F5">
	<?php


	function ca($numb) {
		$st=exec("sudo cat /sys/class/gpio/gpio$numb/value");
		if($st == '0') {
			$st="Включено";
		} else if($st == '1') {
			$st="Выключено";
		} else {
			$st="Проверьте 'Export'";
		}
		echo $st;
	}

	function power($numb) {
		system("sudo bash -c \"echo 0 > /sys/class/gpio/gpio$numb/value\"");
	}

	function powoff($numb) {
		system("sudo bash -c \"echo 1 > /sys/class/gpio/gpio$numb/value\"");
	}

	function res($numb) {
		$st=exec("sudo cat /sys/class/gpio/gpio$numb/value");
		if($st == 0) {
			system("sudo bash -c \"echo 1 > /sys/class/gpio/gpio$numb/value\"");
			sleep(3);
			system("sudo bash -c \"echo 0 > /sys/class/gpio/gpio$numb/value\"");
		}
	}
	
	if(isset( $_GET['res1'] ) ) {
		
                res(5);
        }
	if(isset( $_GET['res2'] ) ) {
                res(6);
        }
	if(isset( $_GET['res3'] ) ) {
                res(13);
        }
	if(isset( $_GET['res4'] ) ) {
                res(19);
        }
	if(isset( $_GET['res'] ) ) {
		$st1=exec("sudo cat /sys/class/gpio/gpio5/value");
		$st2=exec("sudo cat /sys/class/gpio/gpio6/value");
		$st3=exec("sudo cat /sys/class/gpio/gpio13/value");
		$st4=exec("sudo cat /sys/class/gpio/gpio19/value");
		
		if($st1 == 0 && $st2 == 0 && $st3 == 0 && $st4 == 0) {	
			system("sudo ../relay.sh 1");
			sleep(3);
			system("sudo ../relay.sh 0");
		}
        }



	if(isset( $_GET['off1'] ) ) {
		powoff(5);
	}
	if(isset( $_GET['off2'] ) ) {
		powoff(6);
	}
	if(isset( $_GET['off3'] ) ) {
		powoff(13);
	}
	if(isset( $_GET['off4'] ) ) {
		powoff(19);
	}

	if(isset( $_GET['on1'] ) ) {
		power(5);
	}
	if(isset( $_GET['on2'] ) ) {
		power(6);
	}
	if(isset( $_GET['on3'] ) ) {
		power(13);
	}
	if(isset( $_GET['on4'] ) ) {
		power(19);
	}

	if( isset( $_GET['on'] ) ) {
		system("sudo ../relay.sh 0");
	}
	if( isset( $_GET['off'] ) ) {
		system("sudo ../relay.sh 1");
	}
	?> 

	<center><p><h2>Управление питанием</h2></p></center>

	<table border="1">
	<tr><th>№</th><th>Статус</th><th>Включить</th><th>Выключить</th><th>Перезагрузить</th></tr>
	<tr><td>1</td><td><?php ca(5);?></td><td>
	<form method="GET">
		<input type="submit" name="on1" value="вкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="off1" value="выкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="res1" value="res" />
	</form>
	</td></tr>
	<tr><td>2</td><td><?php ca(6);?></td><td>
	<form method="GET">
		<input type="submit" name="on2" value="вкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="off2" value="выкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="res2" value="res" />
	</form>
	</td></tr>
	<tr><td>3</td><td><?php ca(13);?></td><td>
	<form method="GET">
		<input type="submit" name="on3" value="вкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="off3" value="выкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="res3" value="res" />
	</form>
	</td></tr>
	<tr><td>4</td><td><?php ca(19);?></td><td>
	<form method="GET">
		<input type="submit" name="on4" value="вкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="off4" value="выкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="res4" value="res" />
	</form>
	</td></tr>
	<tr><td>Все</td><td>---</td><td>
	<form method="GET">
		<input type="submit" name="on" value="вкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="off" value="выкл" />
	</form>
	</td><td>
	<form method="GET">
		<input type="submit" name="res" value="res" />
	</form>
	</td></tr>

	</body>
</html>

	
