from gpiozero import Button, LED
from signal import pause

button = Button(14)
led = LED(4)

"""
def say_hello():
    print("Hello!")

def say_adios():
    print("!Adios!")
"""

button.when_pressed = led.on
button.when_released = led.off

pause()
