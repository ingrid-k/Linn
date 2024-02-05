#Tirar la moneda.

import random

num = random.randint(0, 1)

if num > 0.5:
    print('Heads')
else:
    print('Tails')

#Crear un programa que diga si una nota esta o no aprobada.

grade= 100

if grade > 55:
    print("You passed.")
else:
    print("You failed.")

#Medir el nivel de pH.

ph= int(input("Ingrese un valor entre 0 y 14: "))

if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")

#Crear un programa que pueda responder a cualquier pregunta de Sí o No con una respuesta diferente cada vez.

import random 

question = input('Hazme una pregunta... ')
random_number = random.randint(1, 9)

if random_number == 1:
    print ("Yes - definitely")
elif random_number == 2:
    print ("It is decidedly so")
elif random_number == 3:
    print ("Without a doubt")
elif random_number == 4:
    print("Reply hazy, try again")
elif random_number == 5:
    print("Ask again later")
elif random_number == 6:
    print("Better not tell you now")
elif random_number == 7:
    print("My sources say no")
elif random_number == 8:
    print("Outlook not so good")
else:
    print("Very doubtful")

#Crear un programa que pregunte la altura y los créditos y determine si puede pasar o no.

height = float(input("Cual es tu altura?"))
credits = int(input("Cuantos creditos tienes?"))

if height >= 1.37 and credits >= 10:
    print("Disfruta el viaje!")
elif height < 1.37 and credits >= 10:
    print("No eres lo suficientemente alto") 
elif height >= 1.37 and credits < 10:
    print("No tienes suficientes creditos")
else:
    print("No has cumplido con los requisitos")