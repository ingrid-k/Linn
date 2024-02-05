#!/bin/zsh

opc=0

while [ $opc -ne 4 ] ; do 

clear 

echo "1. Saludar al usuario"
echo "2. Evaluar edad"
echo "3. Crear respaldo"
echo "4. Salir"

read -p "Seleccione una opcion: " opc

case $opc in

	1)clear 
		echo "hola $USER!"
		sleep 2
		;;	
	2)clear
		read -p "ingrese su edad: " edad

		if [ $edad -lt 18 ]
		then 
			echo "es menor de edad"
		else
			echo "es mayor de edad"
		fi
		sleep 2
		;;
	3)clear
		echo Se esta realizando respaldo...
		sleep 2

		mkdir $HOME/Escritorio/Respaldo
		cp -r $HOME/documentos/* $HOME/Escritorio/Respaldo
		;;
	4)clear
		;;
	*)	echo $opc no es una opcion valida
		;;
esac


read -p "Pulse una tecla para continuar... " tecla
done 
