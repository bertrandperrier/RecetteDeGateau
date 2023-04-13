<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<!-- mysql_enregistrement.php -->
<?php
include("header.php");
$db="mes_jeux_videos";
include("db.php");
?>

<html>
<head>
	<meta http-equiv="content-type" content="text/html; charset=UTF-8">
	<META NAME="Author" LANG="fr" CONTENT="Bertrand PERRIER">
	<meta name="google-site-verification" content="tebZAQI9Z1nmfMM7kOdwiy9Jofria86TGzS_BYorR6Q">
	<link rel="shortcut icon" href="favicon.ico" type="images/x-icon">
	<title>Bertrand&gt;Page d'enregistrement</title>
	<?php
	if ($m==1)
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
</head>
<body>

<?php
if ($m==1)
	{ echo("<h1>Mes jeux vid&eacute;os<br>version mobile</h1>"); }
	else
	{ echo("<h1>Mes jeux vid&eacute;os</h1>"); }


if (isset($_POST["q"])) 	{             $q = $_POST["q"]; }
if (isset($_POST["c"])) 	{             $c = $_POST["c"]; }
if (isset($_POST["name"])) 	{          $name = $_POST["name"]; }
if (isset($_POST["new_id"])) 	{        $new_id = $_POST["new_id"]; }
if (isset($_POST["console"])) 	{       $console = $_POST["console"]; }
if (isset($_POST["developpeur"])) { $developpeur = $_POST["developpeur"]; }
if (isset($_POST["mdp"])) 	{           $mdp = $_POST["mdp"]; }

// premier affichage de la page (pas de validation)
if (!isset($_POST["name"]))
	{
	//sql nb enregistrement
	$sql_list_jv="select id from list_jv;";
	$result_list_jv = $connexion->prepare($sql_list_jv);
	$result_list_jv->execute();	
	$nb_enregistrement_list_jv = count($result_list_jv->fetchAll());
	//sql liste console
	$sql_console="select name, id from console order by name;";
	$result_console = $connexion->prepare($sql_console);
	$result_console->execute();	
	$nb_enregistrement_console = count($result_console->fetchAll());
	//sql liste developpeur
	$sql_developpeur="select name, id from developpeur order by name;";
	$result_developpeur = $connexion->prepare($sql_developpeur);
	$result_developpeur->execute();	
	$nb_enregistrement_developpeur = count($result_developpeur->fetchAll());
				
	//echo 'Il y a '.$nb_enregistrement_list_jv.' enregistrements.<br>';
	//echo 'Il y a '.$nb_enregistrement_console.' consoles.<br>';
	//echo 'Il y a '.$nb_enregistrement_developpeur.' developpeurs.<br>';
		
	//FORM
	echo '<form name="nameFormInscription" action='.$_SERVER["PHP_SELF"].' method="POST">';
	//NOM
	echo '<p class="corps"><table class="TableMarge" align="center">';
	
	//NEW ID HIDDEN
	$new_id = $nb_enregistrement_list_jv+1;
	if ($m != 1) echo '<tr><td>Nom</td><td>Console</td><td>D&eacute;veloppeur</td><td>Mot de passe</td></tr>';
	print '<input id="prodId" name="new_id" type="hidden" value="'.($new_id).'">';
	echo '<tr><td><input type="text" name="name"></td>';
	if ($m==1) echo'</tr><tr>';
	print "<td><select name=\"console\">";
	//CONSOLE
    	foreach ($connexion->query($sql_console) as $ligne_de_tableau)
		{				
       		print '<option value="'.$ligne_de_tableau[1].'">'.$ligne_de_tableau[0].'</option>';
       	    	}
	echo '</select></td>';
	if ($m==1) echo'</tr><tr>';
	//DEVELOPPEUR
	print "<td><select name=\"developpeur\">";
    	foreach ($connexion->query($sql_developpeur) as $ligne_de_tableau)
		{				
       		print '<option value="'.$ligne_de_tableau[1].'">'.$ligne_de_tableau[0].'</option>';
       	    		}
	echo '</select></td>';
	if ($m==1) echo'</tr><tr>';
	//BOUTON ENREGISTRER
	echo '<td><input type="password" name="mdp"><button type="submit">Enregistrer</button></td>';
	echo '</form></tr></table>';
	$result_console->closeCursor();
	$connexion = null; //On ferme la connexion à MySQL
	}

//deuxième affichage de la page (clic sur le bouton Enregistrer)
if (isset($_POST["new_id"]))
	{
	if ($mdp=="KvnzRyuquf6cXRJ%")
		{
		//requete
		$sql_new_game="insert into list_jv values ('".$new_id."', '".$name."','".$console."','".$developpeur."');<br>";
		$result_new_game = $connexion->prepare($sql_new_game);
		$result_new_game->execute();
		$connexion = null; //On ferme la connexion à MySQL
		echo '<p>Enregistr&eacute;<br>';
		echo '<a href="mesjeuxvideos.php?q=1">Voir les enregistrements</a></p>';
		}
	else
		{
		echo '<p class="corps">Mot de passe incorrect</p>';
		}
	}



echo '<h3><a href="'.$_SERVER["PHP_SELF"].'">Recommencer</a><br>';
echo '<a href="page_mesjeuxvideos.php?q=1">Retour &agrave; la liste des jeux</a></h3>';


include("aff_icone.php");
include("copyright.txt");
?>



</body>
</html>
