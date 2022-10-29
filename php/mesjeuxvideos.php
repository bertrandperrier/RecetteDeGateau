<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<!-- mesjeuxvideos.php -->
<?php

$nom_php = __FILE__;
include("header.php");
include("db.php");
?>

<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=UTF-8">
	<META NAME="Author" LANG="fr" CONTENT="Bertrand PERRIER">
	<meta name="google-site-verification" content="tebZAQI9Z1nmfMM7kOdwiy9Jofria86TGzS_BYorR6Q">
	<link rel="shortcut icon" href="favicon.ico" type="images/x-icon">
	<title>Bertrand&gt;Page d'accueil</title>
	<?php
	if (isMobile() || $m==1)
		{
		echo('<link rel="stylesheet" href="style-mobi.css">
			  <link rel="stylesheet" href="blocnotes-mobi.css">');
		}
		else
		{
		echo('<link rel="stylesheet" href="style.css">');
		}
	?>
	<META NAME="Author" LANG="fr" CONTENT="Bertrand PERRIER">
	<meta name="Description" content="Page personnelle de Bertrand Perrier">
	<meta name="Keywords" content="bertrand, perrier, linux, script, ubuntu, cv, informatique, aide, personne, auxiliaire, vie">
	<meta name="Author" content="Bertrand Perrier">
	<meta name="Publisher" content="Bertrand Perrier">
	<meta name="Copyright" content="Copyright © 2009 Bertrand Perrier. Tous droits réservés.">
	<meta name="Content-language" content="fr">
	<meta name="verify-v1" content="tPA7nyIPnaxLqa7J7+PIDRQjO1fffWD+Kbr3m03DA2Q=">
	
	<link rel="alternate" type="application/atom+xml" title="Atom 1.0" href="flux.xml">

</head>
<body>

<?php



if ($m==1)
	{
	echo("<h1>Mes jeux vid&eacute;os<br>version mobile</h1>");
	}
	else
	{
	echo("<h1>Mes jeux vid&eacute;os</h1>");
	}
	
	
	if (!$m==1) {echo '<div class="div_menu">';}
	echo '<p class="center"><b>Voir</b>';
	echo '<p class="center" class="corp_menu"><a href="mesjeuxvideos.php?q=1">tout</a><br>';
	echo '<a href="mesjeuxvideos.php?q=2">les consoles</a><br>';
	echo '<a href="mesjeuxvideos.php?q=3">les developpeurs</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=1">PSX</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=2">SNes</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=3">amiga cd32</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=4">DreamCast</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=5">PC</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=6">Nes</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=7">Switch</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=8">Master System</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=9">N64</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=10">PS3</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=11">Wii</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=12">3DS</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=13">Xbox 360</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=14">Playstation 2</a><br>';
	echo '<a href="mesjeuxvideos.php?q=4&amp;c=15">Game Boy</a></p>';
	echo '<p class="center" class="corp_menu"><a href="mysql_enregistrement.php">Entrer un<br>nouveau jeux<br>id&eacute;o</a></p>';
	if ($m!=1) {echo '</div>';}
	




	if (isset($_GET["q"]))
		{
		$q = $_GET["q"];
		}
	if (isset($_GET["c"]))
		{
		$c = $_GET["c"];
		}
		
			

	include("aff_icone.php");
	if (isset($_GET["q"]) and $q<=4)
		{
		if ($q==1) {$sql="select list_jv.name, console.name, developpeur.name from list_jv join console on list_jv.console = console.id join developpeur on list_jv.developpeur = developpeur.id order by list_jv.name;";}
		if ($q==2) {$sql="select name, id from console order by name;";}
		if ($q==3) {$sql="select name, id from developpeur;";}
		if ($q==4) {$sql="select list_jv.name, console.name, developpeur.name, list_jv.id from list_jv join console on list_jv.console = console.id join developpeur on list_jv.developpeur = developpeur.id where console.id = '$c' order by list_jv.name;";}
		if ($q==5) {$sql="select list_jv.name, console.name, developpeur.name, list_jv.id from list_jv join console on list_jv.console = console.id join developpeur on list_jv.developpeur = developpeur.id order by console;";}
		$result = $connexion->prepare($sql);
		$result->execute();
		// $nb_colonne=$result->columnCount();
		$nb_enregistrement = count($result->fetchAll());
		echo '<p class="corps">Il y a '.$nb_enregistrement.' enregistrement(s).</p>';
		// echo 'Il y a '.$nb_colonne.' colonne(s).<br>';
		echo '<table border=1 class="center"><tr>';
		if ($q == 1) {print "<td><b>Nom</b></td><td><b>Console</b></td><td><b>Developpeur</b></td>";}
		if ($q == 2) {print "<td><b>Nom</b></td><td><b>id</b></td>";} //and ($q!=3 and $q!=2)	
		if ($q == 3) {print "<td><b>Nom</b></td><td><b>id</b></td>";} //and ($q==3 or $q==2)
		if ($q == 4) {print "<td><b>Nom</b></td><td><b>Console</b></td><td><b>developpeur</b></td><td><b>Ref</b></td>";}
		echo '</tr>';
    		foreach ($connexion->query($sql) as $ligne_de_tableau)
			{		
			print "<tr>";
       			if ($q == 1) {print "<td><p class=\"table\"><b>$ligne_de_tableau[0]</b></p></td>
       					     <td><img class=\"logo\" src=\"images/$ligne_de_tableau[1]\" \/></td>
       					     <td><p class=\"table\">$ligne_de_tableau[2]</p></td>
       					     ";}
       			if ($q == 2) {print "<td><img class=\"logo\" src=\"images/$ligne_de_tableau[0]\" \/></td>
       					     <td><p class=\"table\">$ligne_de_tableau[1]</p></td>
       					     ";}
       			if ($q == 3) {print "<td><p class=\"table\">$ligne_de_tableau[0]</p></td>
       					     <td><p class=\"table\">$ligne_de_tableau[1]</p></td>
       					     ";}
       			if ($q == 4) {print "<td><p class=\"table\">$ligne_de_tableau[0]</p></td>
       					     <td><img class=\"logo\" src=\"images/$ligne_de_tableau[1]\" \/></td>
       					     <td><p class=\"table\">$ligne_de_tableau[2]</p></td>
       					     <td><p class=\"table\">$ligne_de_tableau[3]</p></td>
       					     ";}
      
        		print "</tr>";
        		}
		echo '</table>';
		
		$connexion = null; //On ferme la connexion à MySQL
		}

if (!isset($_GET["q"])or $q>4)
	{
	echo '<p class="corps">Choisir dans le menu <b>Voir</b></p>';
	}
	
include("aff_icone.php");
?>
	<p class="alignright">
		<a href="http://validator.w3.org/check?uri=referer"><img
		src="http://www.w3.org/Icons/valid-html401" alt="Valid HTML 4.01 Transitional" height="31" width="88"></a>
	</p>
	

<?php	
include("copyright.txt");
?>

</body>
</html>
