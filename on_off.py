from gpiozero import DigitalOutputDevice
from time import sleep

switch = DigitalOutputDevice(4)

while True:
    switch.on()
    sleep(1)
    switch.off()
    sleep(1)
