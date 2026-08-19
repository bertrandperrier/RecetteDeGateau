#!/bin/bash
echo "===arret du service au démarrage==="
sudo systemctl disable $1
echo "===fin==="
