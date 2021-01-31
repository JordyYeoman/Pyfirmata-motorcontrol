import pyfirmata
import time

board = pyfirmata.Arduino("/dev/cu.usbmodem14201")

it = pyfirmata.util.Iterator(board)
it.start()

board.digital[10].mode = pyfirmata.INPUT

ON = 1
OFF = 0
timeSleep = 0.25


def blink():
    board.digital[13].write(ON)
    print("Light now on with value of " + str(ON))
    time.sleep(timeSleep)

    board.digital[13].write(OFF)
    print("Light now off with value of " + str(OFF))
time.sleep(timeSleep)


while True:
    sw = board.digital[10].read()
    if sw is True:
        board.digital[13].write(1)
    else:
        # board.digital[13].write(0)
        blink()

    time.sleep(0.1)