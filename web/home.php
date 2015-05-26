<html>
	<head>
		<meta charset="utf-8">
		<title>Главная страница</title>
	</head>

	<body bgcolor="#F5F5F5">
	<center>
		<p><h2>Устройство управления розеточкой</h2></p>
		<p>Ip addr: <?php
		system("echo `/sbin/ifconfig eth0 2>/dev/null|awk '/inet addr:/ {print $2}'|sed 's/addr://'`");
		?></p>
		<p>Mask: <?php
		system("echo `/sbin/ifconfig eth0 2>/dev/null|awk '/inet addr:/ {print $4}'|sed 's/Mask://'`");
		?></p>
		<p>Mac addr: <?php
                system("echo `/sbin/ifconfig eth0 2>/dev/null|awk '/HWaddr/ {print $5}'|sed 's/HWaddr//'`");
		?></p>

	<FORM action=home.php method=POST>
        <INPUT Type="submit" name="submit"  VALUE="Обновить страницу"/>
        </FORM>
	</center>
	</body>
</html>
