from mote import Mote
from threading import Thread, Lock
import time
import math
import random

mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)
mote.clear()


class Raindrop:
    def __init__(self, channel):
        self.channel = channel
        self.startTime = time.time()
        self.position = 0
        self.red = random.randint(0, 255)
        self.blue = random.randint(0, 255)
        self.green = random.randint(0, 255)

    def updatePosition(self):
        timeDelta = time.time() - self.startTime
        # s = s0 + v0 + 1/2at^2
        position = (50 * timeDelta) + (0.5 * 9.8 * math.pow(timeDelta, 2))
        normalisedPosition = math.floor(position / 2)
        self.position = normalisedPosition


def drawRaindrops(raindrops, run, lock):
    print("in thread start")
    while run:
        mote.clear()

        lock.acquire()
        print("in thread lock acquired")
        try:
            for raindrop in raindrops:
                raindrop.updatePosition()

                if raindrop.position < 16:
                    mote.set_pixel(raindrop.channel,
                                   raindrop.position, raindrop.red, raindrop.green, raindrop.blue)
                else:
                    raindrops.remove(raindrop)

                mote.show()

        finally:
            lock.release()
            print("in thread lock released")

        print("in thread sleeping")
        time.sleep(1 / 60)
        print("in thread awake")


raindrops = []
run = True
lock = Lock()

try:
    t = Thread(target=drawRaindrops, args=(raindrops, run, lock))
    t.start()

    print("after started")

    while True:
        lock.acquire()
        # print("main lock acquired")
        raindrops.append(Raindrop(random.randint(1, 4)))
        # print(len(raindrops))
        lock.release()
        # print("main lock released")
        time.sleep(random.randint(100, 1000) / 1000)

except KeyboardInterrupt:
    run = False
    mote.clear()
    mote.show()
finally:
    lock.release()
