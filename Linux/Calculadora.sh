#!/bin/zsh

clear

#los valores son pasados por parametros

#numA=$1
#numB=$2

numA=0
numB=0
#defino las varriables y las inicializo

read -p "Ingrese el operando A: " numA
read -p "Ingrese el operando B: " numB

#Operaciones aritmeticas basicas

echo "/////Calculadora/////"
echo "Numeros A=$numA y B=$numB"
echo "Sumar A + B = $((numA + numB))"
echo "Restar A - B = $((numA - numB))"
echo "Dividir A / B = $((numA / numB))"
echo "Multiplicar A * B = $((numA * numB))"
echo "Residuo A % B = $((numA % numB))"

#Operaciones relacionales

echo "A>B= $((numA > numB))"
echo "A<B= $((numA < numB))"
echo "A>=B $((numA >= numB))"
echo "A<=B $((numA <= numB))"
echo "A==B $((numA == numB))"
echo "A!=B $((numA != numB))"





