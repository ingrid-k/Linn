import datetime
import time

def set_alarm(hour, minute):
    while True:
        now = datetime.datetime.now()
        if now.hour == hour and now.minute == minute:
            print("¡Alarma!")
            break
        time.sleep(30)  # Comprobar cada 30 segundos

# Establecer la hora y minuto para la alarma
hora_alarma = int(input("Introduce la hora de la alarma (formato 24h): "))
minuto_alarma = int(input("Introduce el minuto de la alarma: "))

# Llamar a la función para establecer la alarma
set_alarm(hora_alarma, minuto_alarma)
