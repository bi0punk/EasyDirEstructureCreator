from plyer import notification
import psutil
from time import sleep
while True:
    battery = psutil.sensors_battery()
    life = battery.percent
    print(life)
    print(type(life))
    if life > 80 or 50:
        notification.notify(
            title = "bateria baja",
            message = "conectar eneregis",
            timeout = 10
        )
    sleep(60)