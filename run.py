import pyfirmata
import time

board = pyfirmata.Arduino("/dev/cu.usbmodem14201")

ON = 1
OFF = 0
timeSleep = 0.25

while True:
    board.digital[13].write(ON)
    print("Light now on with value of " + str(ON))
    time.sleep(timeSleep)

    board.digital[13].write(OFF)
    print("Light now off with value of " + str(OFF))
    time.sleep(timeSleep)