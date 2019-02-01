from mote import Mote
import time

mote = Mote()
mote.configure_channel(1, 16, False)
mote.configure_channel(2, 16, False)
mote.configure_channel(3, 16, False)
mote.configure_channel(4, 16, False)


def set_pixel(chan, pixel):
    if chan >= 1 and chan <= 4 and pixel >= 0 and pixel <= 15:
        mote.set_pixel(chan, pixel, 255, 255, 255, 0.3)


def A(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(1, start - 2)
    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(1, start - 1)
    set_pixel(3, start - 1)

def B(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(2, start - 1)
    set_pixel(4, start - 1)

def C(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(1, start - 1)
    set_pixel(1, start - 2)
    set_pixel(4, start - 1)
    set_pixel(4, start - 2)

def D(start):
    set_pixel(1, start - 2)
    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(2, start - 1)
    set_pixel(4, start - 1)

# def E(start):
#     set_pixel(1, start)
#     set_pixel(2, start)
#     set_pixel(3, start)
#     set_pixel(4, start)

#     set_pixel(1, start - 1)
#     set_pixel(2, start - 1)
#     set_pixel(1, start - 2)
#     set_pixel(2, start - 2)

#     set_pixel(4, start - 1)
#     set_pixel(4, start - 2)

def F(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(1, start - 1)
    set_pixel(1, start - 2)

    set_pixel(3, start - 1)

def G(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(1, start - 1)
    set_pixel(4, start - 1)

    set_pixel(1, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

def H(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(2, start - 1)

def I(start):
    set_pixel(1, start)
    set_pixel(1, start - 1)
    set_pixel(1, start - 2)

    set_pixel(4, start)
    set_pixel(4, start - 1)
    set_pixel(4, start - 2)

    set_pixel(2, start - 1)
    set_pixel(3, start - 1)

def J(start):
    set_pixel(1, start)
    set_pixel(1, start - 1)
    set_pixel(1, start - 2)

    set_pixel(4, start)
    set_pixel(4, start - 1)

    set_pixel(2, start - 1)
    set_pixel(3, start - 1)

def K(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(2, start - 1)
    set_pixel(3, start - 1)

    set_pixel(1, start - 2)
    set_pixel(4, start - 2)

def L(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(4, start - 1)
    set_pixel(4, start - 2)

def M(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(1, start - 2)
    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(2, start - 1)

def N(start):
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(2, start - 1)

def O(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(1, start - 2)
    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(1, start - 1)
    set_pixel(4, start - 1)

def P(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(1, start - 2)
    set_pixel(2, start - 2)
    set_pixel(3, start - 2)

    set_pixel(1, start - 1)
    set_pixel(3, start - 1)

def Q(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)

    set_pixel(1, start - 2)
    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(1, start - 1)
    set_pixel(3, start - 1)

def R(start):
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(2, start - 1)
    set_pixel(2, start - 2)

# def S(start):

def T(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(4, start - 1)
    set_pixel(4, start - 2)

    set_pixel(2, start - 1)

def U(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(1, start - 2)
    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(4, start - 1)

def V(start):
    set_pixel(2, start)
    set_pixel(3, start)

    set_pixel(2, start - 2)
    set_pixel(3, start - 2)

    set_pixel(4, start - 1)

def W(start):
    set_pixel(1, start)
    set_pixel(2, start)
    set_pixel(3, start)
    set_pixel(4, start)

    set_pixel(1, start - 2)
    set_pixel(2, start - 2)
    set_pixel(3, start - 2)
    set_pixel(4, start - 2)

    set_pixel(3, start - 1)

def X(start):
    set_pixel(2, start)
    set_pixel(3, start - 1)
    set_pixel(4, start - 2)

    set_pixel(2, start - 2)
    set_pixel(3, start - 1)
    set_pixel(4, start)

def Y(start):
    set_pixel(1, start)
    set_pixel(1, start - 2)

    set_pixel(2, start - 1)
    set_pixel(3, start - 1)
    set_pixel(4, start - 1)

def Z(start):
    set_pixel(2, start)
    set_pixel(2, start - 1)
    set_pixel(2, start - 2)

    set_pixel(4, start)
    set_pixel(4, start - 1)
    set_pixel(4, start - 2)

    set_pixel(3, start - 1)

alphabet = {
      "A": A,
      "B": B,
      "C": C,
      "D": D,
      # "E": E,
      "F": F,
      "G": G,
      "H": H,
      "I": I,
      "J": J,
      "K": K,
      "L": L,
      "M": M,
      "N": N,
      "O": O,
      "P": P,
      "Q": Q,
      "R": R,
      # "S": S,
      "T": T,
      "U": U,
      "V": V,
      "W": W,
      "X": X,
      "Y": Y,
      "Z": Z
    }

mote.clear()


text = input("type something (can't use E or S)\n")

startPosition = 0
printing = True

while printing:
    mote.clear()
    offset = 0

    for letter in range(len(text)):
        position = startPosition - (letter * 4)
        character = text[letter].upper()
        if character != " ":
          alphabet[character](position)
    
    mote.show()
    startPosition += 1
    time.sleep(1 / 8)
    
    if startPosition - (len(text) * 4) > 15:
        printing = False


mote.clear()
mote.show()