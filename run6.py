from pyfirmata import Arduino, util
from time import sleep

board = Arduino("/dev/cu.usbserial-1410")  # Change to your port
ledPin = board.get_pin("d:11:p")  # PWM Pin
print("Starting to output PWM signal")
while True:

    ledPin.write(50)
    sleep(2)
    ledPin.write(0)
    sleep(2)
