<html>
	<head>
		<meta charset="utf-8"/>
		<meta http-equiv="refresh" content="60" />
	</head>
	

	<body bgcolor="#F5F5F5">
	<center>
	<p><h2>Информация об устройстве</h2></p>
	<br>
	<?php
	system("date");?>
	<br>
	<br>
	<h2><pre>
	<?php
	system("sudo ifconfig eth0");
	?></pre></h2>
	<br>
	<br>
	<br>
	<FORM action=info.php method=POST>
	<INPUT Type="submit" style="background-image: url(button_refresh.png); width: 127px; height: 127px; border: none;"  name="submit"  value="Обновить"/>
	</FORM>
	</center>
	</body>
</html>
