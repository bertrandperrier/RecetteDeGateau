<?php
try
	{
	$connexion = new PDO("mysql:host=localhost;port=8889;dbname=my_db_name", 'my_user_name', 'my_password');
	$connexion->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
	}
catch(PDOException $e)
	{
	echo "Connection failed: " . $e->getMessage();
	}
?>
