import pyfirmata
import time

board = pyfirmata.Arduino("/dev/cu.usbserial-1410")
it = pyfirmata.util.Iterator(board)
it.start()

# Reading input from Analog Pin 2
analog_input = board.get_pin("a:2:i")

while True:
    analog_value = analog_input.read()
    print(analog_value)
    time.sleep(0.1)
    if analog_value is None:
        analog_value = 0
    elif analog_value > 0.6:
        board.digital[13].write(1)
        print("Light now on with value of " + str(analog_value))
    else:
        board.digital[13].write(0)