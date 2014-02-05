#!/bin/bash
echo "===arret du service au démarrage==="
sudo update-rc.d -f $1 remove
echo "===fin==="
