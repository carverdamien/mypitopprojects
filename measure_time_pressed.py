import sys
from gpiozero import Button, Buzzer
import time

button = Button(int(sys.argv[1]))
buzzer = Buzzer(int(sys.argv[2]))

begin=0
end=0

while True:
    if button.is_pressed:
        buzzer.on()
        if begin==end:
            begin = time.time()
        else:
            end = time.time()
    else:
        buzzer.off()
        if end!=begin:
            print(end-begin)
            begin = end
    
