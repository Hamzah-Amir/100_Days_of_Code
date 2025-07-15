# Write a program that reminds user to drink water after every hour

import time
from plyer import notification
import winsound

winsound.MessageBeep()

while True:
    time.sleep(3600)
    winsound.PlaySound("SystemAsterisk", winsound.SND_ALIAS)
    notification.notify(
        app_name = "💧 Hydration Reminder",
        title="💧 Time to drink water!",
        message= "Drink a glass of Water",
        timeout =  5
    )