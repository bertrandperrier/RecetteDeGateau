<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<!-- mesjeuxvideos.php -->
<?php
include("header.php");
$db="mes_jeux_videos";
include("db.php");
?>
<meta name="Description" content="Mes jeux vidéos">
<title>Bertrand&gt;Page d'accueil</title>
<script src="sommaire_cache.js" type="text/javascript"></script>
</head>
<body>

<?php

	if ($m==1)
		{
		include("aff_icone.php");
		}

if ($m==1)
	{
	echo("<h1>Mes jeux vid&eacute;os<br>version mobile</h1>");
	}
	else
	{
	echo("<h1>Mes jeux vid&eacute;os</h1>");
	// afficher le sous menu en haut à droite
	echo('	<div class="div_menu" id="id_div_sommaire">
	<div class="id_div_sommaire_haut" id="id_div_sommaire_haut">');
	}


	echo "<p class='center'><b>Voir</b>\n";
	echo "<p class='center corp_menu'>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=1>par nom</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=6>par developpeurs</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=2>les consoles</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=3>les developpeurs</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=1>PSX</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=2>SNes</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=3>amiga cd32</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=4>DreamCast</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=5>PC</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=6>Nes</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=7>Switch</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=8>Master System</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=9>N64</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=10>PS3</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=11>Wii</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=12>3DS</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=13>Xbox 360</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=14>Playstation 2</a><br>\n";
	echo "<a href=".basename($_SERVER["PHP_SELF"])."?q=4&c=15>Game Boy</a></p>\n";
	echo "<p class='center corp_menu'><a href='mysql_enregistrement.php'>Entrer un nouveau jeux vid&eacute;o</a></p>\n";

	if ($m!=1)
		{
		echo('</div>');
		echo('<div class="div_menu_bas" id="div_menu_bas"><p class="alignright"><a class="pointeurmain"  onclick="cache_menu_sommaire();"><img  id="fleche" src="images/croix.png"  alt="fermer"></a></p></div>'); 
		echo('</div>');
		}



	if (isset($_GET["q"]))
		{
		$q = $_GET["q"];
		}
	if (isset($_GET["c"]))
		{
		$c = $_GET["c"];
		}
		
			

	if (isset($_GET["q"]) and $q<=6)
		{
		if ($q==1) {$sql="select list_jv.name, console.name, developpeur.name from list_jv join console on list_jv.console = console.id join developpeur on list_jv.developpeur = developpeur.id order by list_jv.name;";}
		if ($q==2) {$sql="select name, id from console order by name;";}
		if ($q==3) {$sql="select name, id from developpeur order by name;";}
		if ($q==4) {$sql="select list_jv.name, console.name, developpeur.name, list_jv.id from list_jv join console on list_jv.console = console.id join developpeur on list_jv.developpeur = developpeur.id where console.id = '$c' order by list_jv.name;";}
		if ($q==5) {$sql="select list_jv.name, console.name, developpeur.name, list_jv.id from list_jv join console on list_jv.console = console.id join developpeur on list_jv.developpeur = developpeur.id order by console;";}
		if ($q==6) {$sql="select list_jv.name, console.name, developpeur.name from list_jv join console on list_jv.console = console.id join developpeur on list_jv.developpeur = developpeur.id order by developpeur.name;";}
		$result = $connexion->prepare($sql);
		$result->execute();
		// $nb_colonne=$result->columnCount();
		$nb_enregistrement = count($result->fetchAll());
		echo '<p class="corps">Il y a '.$nb_enregistrement.' enregistrement(s).</p>';
		// echo 'Il y a '.$nb_colonne.' colonne(s).<br>';
		echo '<table border=1 class="center"><tr>';
		if ($q == 1 or $q == 6) {print "<td><b>Nom</b></td><td><b>Console</b></td><td><b>Developpeur</b></td>";}
		if ($q == 2) {print "<td><b>Nom</b></td><td><b>id</b></td>";} //and ($q!=3 and $q!=2)	
		if ($q == 3) {print "<td><b>Nom</b></td><td><b>id</b></td>";} //and ($q==3 or $q==2)
		if ($q == 4 && $c == 7) {print "<h2><a href=\"page_captures_d_ecran.php\">Mes captures d'&eacute;cran</a></h2>";}
		if ($q == 4) {print "<td><b>Nom</b></td><td><b>Console</b></td><td><b>developpeur</b></td><td><b>Ref</b></td>";}
		echo '</tr>';
    		foreach ($connexion->query($sql) as $ligne_de_tableau)
			{		
			print "<tr>";
       			if ($q == 1 or $q == 6) {print "<td><p class=\"table\"><b>$ligne_de_tableau[0]</b></p></td>
       					     <td><img class=\"logo\" src=\"images/$ligne_de_tableau[1]\" alt=\"nom de la console\"></td>
       					     <td><p class=\"table\">$ligne_de_tableau[2]</p></td>
       					     ";}
       			if ($q == 2) {print "<td><img class=\"logo\" src=\"images/$ligne_de_tableau[0]\" alt=\"nom de la console\"></td>
       					     <td><p class=\"table\">$ligne_de_tableau[1]</p></td>
       					     ";}
       			if ($q == 3) {print "<td><p class=\"table\">$ligne_de_tableau[0]</p></td>
       					     <td><p class=\"table\">$ligne_de_tableau[1]</p></td>
       					     ";}
       			if ($q == 4) {print "<td><p class=\"table\">$ligne_de_tableau[0]</p></td>
       					     <td><img class=\"logo\" src=\"images/$ligne_de_tableau[1]\" alt=\"nom de la console\"></td>
       					     <td><p class=\"table\">$ligne_de_tableau[2]</p></td>
       					     <td><p class=\"table\">$ligne_de_tableau[3]</p></td>
       					     ";}
      
        		print "</tr>";
        		}
		echo '</table>';
		
		$connexion = null; //On ferme la connexion à MySQL
		}

if (!isset($_GET["q"])or $q>6)
	{
	echo '<p class="centre">Choisir dans le menu <b>Voir</b><br><br><br><br><br><br><br><br><br><br><br><br><br><br><br></p>';
	}
	
if ($m!=1)
	include("aff_icone.php");
	else
	echo('</div>');
?>

	

<?php	
include("copyright.txt");
?>

</body>
</html>
