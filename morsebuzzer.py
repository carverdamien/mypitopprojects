import sys
from gpiozero import Buzzer
from morse import alphanum2morse
from time import sleep

buzzer = Buzzer(int(sys.argv[1]))
time = float(sys.argv[2])
alphanum = sys.argv[3]

for i in alphanum2morse(alphanum):
    if i:
        buzzer.on()
    else:
        buzzer.off()
    sleep(time)
