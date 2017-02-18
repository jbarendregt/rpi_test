from gpiozero import Button
from signal import pause

button = Button(14)

def say_hello():
    print("Hello!")

def say_adios():
    print("!Adios!")


button.when_pressed = say_hello
button.when_released = say_adios

pause()
