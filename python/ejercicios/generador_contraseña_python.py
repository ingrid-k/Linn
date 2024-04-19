import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for i in range(longitud))
    return contrasena

longitud = int(input("Ingrese la longitud de la contraseña: "))
contrasena_generada = generar_contrasena(longitud)
print("Contraseña generada:", contrasena_generada)
