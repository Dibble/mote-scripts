from mote import Mote
import time

mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)
mote.clear()
mote.show()

# colours = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
# iteration = 0
red = 255
green = 0
blue = 0

try:
    while True:
        if red > 0 and blue == 0:
            red -= 1
            green += 1
        if green > 0 and red == 0:
            green -= 1
            blue += 1
        if blue > 0 and green == 0:
            blue -= 1
            red += 1

        mote.set_all(red, green, blue, 0.5)
        mote.show()

        time.sleep(0.1)
        # iteration += 1

except KeyboardInterrupt:
    mote.clear()
    mote.show()
