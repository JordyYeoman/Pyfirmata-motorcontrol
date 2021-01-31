import pyfirmata
import time

board = pyfirmata.Arduino("/dev/cu.usbserial-1420")
it = pyfirmata.util.Iterator(board)
it.start()

# Reading input from Analog Pin 2
analog_input = board.get_pin("a:2:i")

while True:
    analog_value = analog_input.read()
    print(analog_value)
    time.sleep(0.1)
