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

#Programa que representa la canción "99 bottles of beer".

for i in range(99, 0, -1):
  print(f"{i} botellas de cerveza en la pared")
  print(f"{i} botellas de cerveza")
  print("toma una y pasala")
  print(f"{i-1} botellas de cerveza en la pared")