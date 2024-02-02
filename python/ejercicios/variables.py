#Crear un programa que convierta grados Fahrenheit a Celsius.

fahrenheit= 28.4
celsius=(fahrenheit - 32) / 1.8
print(celsius)

#Calculadora de IMC.

peso= 65
altura= 1.69
imc=(peso/altura**2)
print(imc)

#Crear un programa que pregunte por dos números y calcule la hipotenusa.

lado_a= int(input("Ingrese un numero: "))
lado_b= int(input("Ingrese otro numero: "))
c = (lado_a**2 + lado_b**2) ** 0.5
print(c)

#Calculadora de cambio de divisas.

co= int(input("Cuanto tienes en pesos colombianos?: "))
pe= int(input("Cuanto tienes en soles?: "))
br= int(input("Cuanto tienes en reales?: "))

dolar_a_co= co * 0.00025
dolar_a_pe= pe * 0.27
dolar_a_br= br * 0.20

usd= int(dolar_a_co + dolar_a_pe + dolar_a_br)
print(usd)