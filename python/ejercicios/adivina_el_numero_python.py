import random

def adivina_el_numero():
    numero_secreto = random.randint(1, 100)
    intentos = 0

    print("¡Bienvenido a Adivina el Número!")
    print("Estoy pensando en un número entre 1 y 100.")

    while True:
        guess = int(input("Introduce tu suposición: "))
        intentos += 1

        if guess < numero_secreto:
            print("El número que estoy pensando es mayor.")
        elif guess > numero_secreto:
            print("El número que estoy pensando es menor.")
        else:
            print(f"¡Felicidades! Adivinaste el número en {intentos} intentos.")
            break

if __name__ == "__main__":
    adivina_el_numero()
