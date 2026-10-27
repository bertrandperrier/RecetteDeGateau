#!/bin/bash

mise_a_jour_rustdesk()
	{
	VERSION=$(curl -s https://api.github.com/repos/rustdesk/rustdesk/releases/latest \
		| grep '"tag_name"' \
		| cut -d '"' -f4)

	if [ -z "$VERSION" ]; then
		echo "Impossible de récupérer la version RustDesk"
		return
	fi

	
	INSTALLEE=$(dpkg-query -W -f='${Version}' rustdesk 2>/dev/null)
	
	if [ -z "$INSTALLEE" ]; then
		echo "RustDesk n'est pas installé"
		return
	fi

	echo "RustDesk installé : $INSTALLEE"
	echo "Dernière version  : $VERSION"

	if [ "$INSTALLEE" = "$VERSION" ]; then
		echo "RustDesk est déjà à jour"
		return
	fi

	echo "Mise à jour de RustDesk vers $VERSION"

	cd /tmp || return

	wget -q \
	"https://github.com/rustdesk/rustdesk/releases/download/$VERSION/rustdesk-$VERSION-x86_64.deb" \
	-O rustdesk.deb

	if [ -f rustdesk.deb ]; then
		sudo apt install -y ./rustdesk.deb
		rm -f rustdesk.deb
	else
		echo "Téléchargement RustDesk échoué"
	fi
	}

if [ `id -u` -ne 0 ]
then
	sh /home/$USER/linux/script/lecteur_fichier.sh
	rm /home/$USER/linux/script/liste_id_email ## effacement du journal des id des messages d'exim
	sudo ls /var/spool/exim4/input >> /home/$USER/linux/script/liste_id_email ## journalise les id des messages d'exim
	message=$(ls -lh /home/$USER/linux/script/liste_id_email | cut -d " " -f5)
	if [ $message -eq 0 ]
	then
		echo "update"
		sudo rm -rf /var/lib/apt/lists/*
		sudo apt -qq update
		echo ""
		echo "upgrade"
		sudo apt -qq upgrade
		echo ""
		echo "dist-upgrade"
		sudo apt -qq dist-upgrade
		echo ""
		echo "snap refresh"
		sudo snap refresh
		echo ""
		echo "autoremove"
		sudo apt -qq autoremove
		echo ""
		echo "list --upgradable"
		apt -qq list --upgradable
		echo "paquets obsoletes"
		apt list ?obsolete
		echo ""
		echo "désinstallation des rev anciennes de snap"
		snap list --all | awk '/désactivé/{print $1, $3}' | while read nom rev; do sudo snap remove "$nom" --revision="$rev"; done
		echo ""
		echo "syslog grep script"
		sh /home/$USER/linux/script/syslog_grep_script.sh
		echo ""
		echo "vérif mise à jour de rustdesk"
		mise_a_jour_rustdesk
	fi
else
	echo "sudo not support"
fi
