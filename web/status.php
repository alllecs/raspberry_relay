<html>
	<head>
		<meta charset="utf-8">
		<meta http-equiv="refresh" content="60" />
		<title>My site</title>
		<style>
		table {
			width: 1000px; /* Ширина таблицы */
			border: 1px solid black; /* Рамка вокруг таблицы */
			margin: auto; /* Выравниваем таблицу по центру окна  */
		}
		td {
			text-align: center; /* Выравниваем текст по центру ячейки */
		}
		</style>
	</head>

	<body text="0000CC" bgcolor="#F5F5F5" link="#33FF00" alink="#CC0099" vlink="#00FFFF">

	<center><p><h2>Просмотр состояния</h2></p></center>
		<?php
		function ca($numb) {
                $st=exec("sudo cat /sys/class/gpio/gpio$numb/value");
                if($st == '0') {
                        $st=1;
                } else if($st == '1') {
                        $st=0;
                } else {
                        $st="Нажмите 'Export'";
                }
                echo $st;
        }


		function expo($numb) {
			system("sudo bash -c 'echo $numb > /sys/class/gpio/export'");
			system("sudo bash -c 'echo high > /sys/class/gpio/gpio$numb/direction'");
		}	
		function unexpo($numb) {
			system("sudo bash -c 'echo $numb > /sys/class/gpio/unexport'");
		}
			if (isset( $_POST['export1'])) {
			expo(5);
			}
			if (isset( $_POST['unexport1'])) {
			unexpo(5);
			}
			if (isset( $_POST['export2'])) {
			expo(6);
			}
			if (isset( $_POST['unexport2'])) {
			unexpo(6);
			}
			if (isset( $_POST['export3'])) {
			expo(13);
			}
			if (isset( $_POST['unexport3'])) {
			unexpo(13);
			}
			if (isset( $_POST['export4'])) {
			expo(19);
			}
			if (isset( $_POST['unexport4'])) {
			unexpo(19);
			}
		?>
		<table border="1">
		<tr><th>№ реле</th><th>Cостояние</th><th>Export</th><th>Unexport</th><th>GPIO</th></tr>
		<tr><td>1</td>
			<td>
			<?php ca(5);?>
			</td>
			<td>
			<form method="POST">
			<input type="submit" name="export1" value="Export 1" />
			</form>
			</td><td>
			<form method="POST">
                        <input type="submit" name="unexport1" value="Unexport 1">
			</form>
			</td><td>5</td></tr>
		<tr><td>2</td>
			<td>
			<?php ca(6);?>
			</td>
			<td>
			<form method="POST">
				<input type="submit" name="export2" value="Export 2" />
			</form>
			</td><td>
			<form method="POST">
                                <input type="submit" name="unexport2" value="Unexport 2" />
			</form>
			</td><td>6</td></tr>
		<tr><td>3</td>
			<td>
			<?php ca(13);?>
			</td>
			<td>
			<form method="POST">
				<input type="submit" name="export3" value="Export 3" />
			</form>
			</td><td>
			<form method="POST">
                                <input type="submit" name="unexport3" value="Unexport 3" />
			</form>
			</td><td>13</td></tr>
		<tr><td>4</td>
			<td>
			<?php ca(19);?>
			</td>
			<td>
			<form method="POST">
				<input type="submit" name="export4" value="Export 4" />
			</form>
			</td><td>
			<form method="POST">
                                <input type="submit" name="unexport4" value="Unexport 4" />
			</form>
			</td><td>19</td></tr>


	</body>
</html>
