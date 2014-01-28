RecetteDeGateau
===============
tuto git
========
clone
-------
ssh-keygen -t rsa -C "<email>"

sudo apt-get install xclip

xclip -sel clip <~/.ssh/id_rsa.pub

sudo apt-get install git

git config --global user.name "prénom nom"

git config --global user.email email

git config --global core.editor geany

git config --list

mkdir -rep de travail-

cd -rep de travail-

git clone git@github.com:-url-.git

use
---
cd git folder's

git pull  // modifier les fichiers

git add <fichier ou dossier>

git status

git commit -m "comment"

git push

pour revenir à la version du dépot

git checkout -- <url fichier>
