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

#Sombrero seleccionador

gryffindor = 0
hufflepuff = 0
ravenclaw = 0
slytherin = 0


q1= print("Do you like Dawn or Dusk? Dawn or Dusk")
respuesta_1 = int(input('Elija 1 o 2: '))

if respuesta_1 == 1:
    gryffindor += 1
    ravenclaw += 1
elif respuesta_1 == 2:
    hufflepuff += 1
    slytherin +=1
else:
    print('Respuesta incorrecta')


q2= print("When Im dead, I want people to remember me as: 1) The Good 2) The Great 3) The Wise 4) The Bold")
respuesta_2 = int(input('Elija un numero entre 1 y 4: '))

if respuesta_2 == 1:
    hufflepuff += 2
elif respuesta_2 == 2:
    slytherin += 2
elif respuesta_2 == 3:
    ravenclaw += 2
elif respuesta_2 == 4:
    gryffindor += 2
else:
    print('Respuesta incorrecta')


q3= print("Which kind of instrument most pleases your ear? 1) The violin 2) The trumpet 3) The piano 4) The drum")
respuesta_3 = int(input('Elija un numero entre 1 y 4: '))

if respuesta_3 == 1:
    slytherin += 4
elif respuesta_3 == 2:
    hufflepuff += 4
elif respuesta_3 == 3:
    ravenclaw +=4
elif respuesta_3 == 4:
    gryffindor += 4
else:
    print('Respuesta incorrecta')

print("Gryffindor: ", gryffindor)
print("Ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

ganador = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if gryffindor == ganador:
    print('¡Tu perteneces a: Gryffindor!')
elif ravenclaw == ganador:
    print('¡Tu perteneces a: Ravenclaw!')
elif hufflepuff == ganador:
    print('¡Tu perteneces a: Hufflepuff!')
else:
    print('¡Tu perteneces a: Slytherin!')