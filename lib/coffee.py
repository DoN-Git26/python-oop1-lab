#!/usr/bin/env python3

class Coffee:
    """A coffee sold by the store."""

    SIZES = ("Small", "Medium", "Large")

    def __init__(self, size, price):
        self.size = size
        self.price = price

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        # Only allow the supported sizes; otherwise print a message
        if value in self.SIZES:
            self._size = value
        else:
            print("size must be Small, Medium, or Large")

    def tip(self):
        print("This coffee is great, here’s a tip!")
        self.price += 1
