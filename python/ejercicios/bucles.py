#Un cajero que pide un PIN.

pin = int(input("Ingrese su PIN: "))

while pin != 1111:
  pin = int(input("PIN incorrecto, ingrese su PIN correctamente: "))

if pin == 1111:
  print("Su PIN es correcto!")

#Adivinar el número.

adivinanzas = 0
intentos = 0

while adivinanzas != 6 and intentos < 5:
  adivinanzas = int(input("Adivina el numero:  "))

print("Lo adivinaste!")

#Bucle for.

for i in range(41):
  print(i)

#Crear un programa que represente la canción "99 bottles of beer".

for i in range(99, 0, -1):
  print(f"{i} botellas de cerveza en la pared")
  print(f"{i} botellas de cerveza")
  print("toma una y pasala")
  print(f"{i-1} botellas de cerveza en la pared")

#Crear un programa que represente el juego llamado "Fizz Buzz".
#Multiplos de 3, imprime Fizz.
#Multiplos de 5, imprime Buzz.
#Multiplos de 3 y 5, imprime Fizz Buzz.

for i in range(1, 101):
  if i % 3 == 0 and i % 5 == 0:
    print('FizzBuzz')
  elif i % 3 == 0:
    print('Fizz')
  elif i % 5 == 0:
    print('Buzz')
  else:
    print(i)
