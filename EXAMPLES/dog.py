from mammal import Mammal

class Dog(Mammal):
    def __init__(self):
        self._breed = None

    def make_sound(self):
        print("Woof! Woof!")

    def wag_tail(self):
        print("wagging...")

