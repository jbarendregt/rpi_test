from gpiozero import Button
from signal import pause

button = Button(14)

def say_hello():
    print("Hello!")

button.when_pressed = say_hello

pause()
