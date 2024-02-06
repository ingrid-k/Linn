#Un cajero que pide un PIN.

pin = int(input('Ingrese su PIN: '))

while pin != 1111:
  pin = int(input('PIN incorrecto, ingrese su PIN correctamente: '))

if pin == 1111:
  print('Su PIN es correcto!')

#Adivinar el número.

adivinanzas = 0
intentos = 0

while adivinanzas != 6 and intentos < 5:
  adivinanzas = int(input('Adivina el numero:  '))

print("Lo adivinaste!")