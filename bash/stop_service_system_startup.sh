#!/bin/bash
echo "===arret du service au démmarage==="
sudo update-rc.d -f $1 remove
echo "===fin==="
