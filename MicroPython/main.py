"""
Created by: Julianne Leblanc-Peltier
Created on: Oct 2023
This module is a Micro:bit MicroPython program which runs stop light colours
"""

from microbit import *

display.clear()
neopixelstrip = neopixel.NeoPixel(pin0, 4)
neopixelstrip[0] = (0, 0, 0)
neopixelstrip[1] = (0, 0, 0)
neopixelstrip[2] = (0, 0, 0)
neopixelstrip[3] = (0, 0, 0)
neopixelstrip.show()
display.show(Image.HAPPY)

while True:
    if button_a.was_pressed():
        display.show(Image.HAPPY)
        neopixelstrip[0] = (0, 255, 0)
        sleep(300)
        neopixelstrip[0] = (0, 0, 0)

        neopixelstrip[1] = (255, 255, 0)
        sleep(200)
        neopixelstrip[1] = (0, 0, 0)

        neopixelstrip[2] = (255, 0, 0)
        sleep(100)
        neopixelstrip[2] = (0, 0, 0)

    if button_b.was_pressed():
        display.show(Image.HAPPY)
        neopixelstrip[0] = (0, 0, 0)
        neopixelstrip[1] = (0, 0, 0)
        neopixelstrip[2] = (0, 0, 0)
        neopixelstrip[3] = (0, 0, 0)
