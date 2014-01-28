test
RecetteDeGateau
===============
tuto git
========
clone
-------
ssh-keygen -t rsa -C "email"

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

// pour vérifier que le dépot n'a pas été modifié

git pull

// modifier les fichiers

git add <fichier ou dossier>

git status

git commit -m "comment"

git push

// pour revenir à la version du dépot

git checkout -- -url fichier-


erreur
======
les fichiers que j'avais pullé puis modifié, ont été modifié par quelqu'un d'autre,

$ git pull

error: Your local changes to the following files would be overwritten by merge:

	README.md
	
Please, commit your changes or stash them before you can merge.

Aborting


$ git commit -m "maj"

# Changes not staged for commit:

#	modified:   README.md

no changes added to commit (use "git add" and/or "git commit -a")


$ git add README.md


$ git commit -m "maj"

[master b20a0d8] maj

 1 file changed, 1 insertion(+)
 
 
$ git pull

Auto-merging README.md

Merge made by the 'recursive' strategy.

 README.md


$ git status

Your branch is ahead of 'origin/master' by 2 commits.

nothing to commit (working directory clean)


$ git push

Writing objects: 100% (6/6), 764 bytes, done.

Total 6 (delta 2)


$ git status

# On branch master

nothing to commit (working directory clean)
