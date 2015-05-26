<html>
	<head>
		<meta charset="utf-8"/>
	</head>
	

	<body>
	<center>
	<p><h2>Информация об устройстве</h2></p>
	<br>
	<?php
	system("date");?>
	<br>
	<br>
	<h3><pre>
	<?php
	system("sudo ifconfig eth0");
	?></pre></h3>
	<br>
	<br>
	<br>
	<FORM action=info.php method=POST>
	<INPUT Type="submit" name="submit"  VALUE="Обновить страницу"/>
	</FORM>
	</center>
	</body>
</html>
