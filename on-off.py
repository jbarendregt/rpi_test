from gpiozero import LED, Button
#from time import sleep
#from random import uniform
from signal import pause

led = LED(4)
right_button = Button(15)
left_button = Button(14)

right_button.when_pressed = led.on()
left_button.when_pressed = led.off()

pause()
