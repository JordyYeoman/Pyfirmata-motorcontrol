#!/usr/bin/env python3
from pyfirmata import Arduino, util
from time import sleep

board = Arduino("/dev/cu.usbserial-1410")  # Change to your port
ledPin = board.get_pin("d:11:p")  # PWM Pin
print("Starting to output PWM signal")
while True:
    for i in range(0, 120, 5):
        ledPin.write(i)
        print(i)
        sleep(0.25)

    sleep(1)
    for i in range(128, 1, -1):
        ledPin.write(i)
        print(i)
        sleep(0.05)
    sleep(1)

    # ledPin.write(120)
    # sleep(0.5)
    # ledPin.write(0)
    # sleep(0.5)