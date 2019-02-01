from mote import Mote

mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)


def french_flag():
    mote.clear()
    for channel in range(1, 5):
        for pixel in range(5):
            mote.set_pixel(channel, pixel, 0, 0, 255, 0.5)
            mote.set_pixel(channel, pixel + 11, 255, 0, 0, 0.5)

        for pixel in range(6):
            mote.set_pixel(channel, pixel + 5, 255, 255, 255, 0.5)

    mote.show()


try:
    while True:
        french_flag()
except KeyboardInterrupt:
    mote.clear()
    mote.show()
