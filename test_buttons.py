from gpiozero import Button, LED
from signal import pause

button1 = Button(14)
button2 = Button(15)
led = LED(4)


button1.when_pressed = led.on
button2.when_pressed = led.off

pause()
