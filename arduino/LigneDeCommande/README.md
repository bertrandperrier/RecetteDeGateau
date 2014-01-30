à partir de https://github.com/sudar/Arduino-Makefile

copier les fichiers Arduino.mk  Common.mk dans un repertoire de travail

à partir du repertoire de travail

créer et se placer dans le repertoire du projet

mkdir MonProjet && cd MonProjet

crée un fichier "Makefile" et copier le contenu ci-dessous

---------------------------------

BOARD_TAG    = uno


ARDUINO_DIR = /usr/share/arduino

ARDMK_DIR = ../

AVR_TOOLS_DIR = /usr


AVRDDUDE     = /usr/bin/avrdude

AVRDUDE_CONF = /etc/avrdude.conf


include ../Arduino.mk

---------------------------------


ajouter #include \<Arduino.h\> dans le cpp

make

un dossier "build-uno" est crée

Pour une carte arduino de type uno

avrdude -v -p m328p -P /dev/ttyACM0 -b115200 -c arduino -U flash:w:build-uno/\<nom du fichier\>.hex

le programme a été transféré dans la carte arduino
