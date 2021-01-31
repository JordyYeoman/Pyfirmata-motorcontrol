import pyfirmata
import time

board = pyfirmata.Arduino("/dev/cu.usbserial-1420")

it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin("a:2:i")
led = board.get_pin("d:11:p")

while True:
    analog_value = analog_input.read()
    if analog_value is None:
        analog_value = 0
    elif analog_value > 0.01:
        led.write(analog_value)
        print(analog_value)
        time.sleep(0.1)
    else:
        led.write(0)
        print("Analog Value too low!")