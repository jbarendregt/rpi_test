from gpiozero import Button, LED
from signal import pause

switch = DigitalOutputDevice(4)

while True:
    switch.on()
    sleep(1)
    switch.off()
    sleep(1)
