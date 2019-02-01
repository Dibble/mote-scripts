from mote import Mote
import random
import time

m = Mote()
m.set_clear_on_exit(True)
m.configure_channel(1, 16, False)
m.configure_channel(2, 16, False)
m.configure_channel(3, 16, False)
m.configure_channel(4, 16, False)
m.clear()

try:
    while True:
        clear = random.randint(0, 9)
        if clear == 0:
            m.clear()

        for channel in range(1, 5):
            pixel = random.randint(0, 15)
            red = random.randint(0, 255)
            green = random.randint(0, 255)
            blue = random.randint(0, 255)
            delay = random.randint(2, 20)

            m.set_pixel(channel, pixel, red, green, blue, 0.5)

        m.show()

        time.sleep(delay / 1000)


except KeyboardInterrupt:
    m.clear()
    m.show()
