from gpiozero import LED, Buzzer, Button
from time import sleep

led = LED(4)
buzz = Buzzer(13)
but = Button(27)

while True:
    if but.is_pressed:
        buzz.on()
        led.off()
    else:
        led.on()
        buzz.off()


