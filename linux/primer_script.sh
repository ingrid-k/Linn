#!/bin/zsh

echo "Hola Taylor"

nombre="Taylor"

echo "Mi nombre es $nombre"

#Exporto la variable nombre

export nombre

echo "Voy a llamar a otro script"

sleep 3;
./segundo_script.sh

