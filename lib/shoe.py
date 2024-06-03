#!/usr/bin/env python3

class Shoe:
    def __init__(self, brand, size):
        self.brand = brand
        self._size = None
        self.size = size  
        self.condition = "Used"  

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if isinstance(value, int):
            self._size = value
        else:
            print("size must be an integer")

    @property
    def brand(self):
        return self._brand

    @brand.setter
    def brand(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 50:
            self._brand = value
        else:
            raise ValueError("Brand must be a string between 1 and 50 characters.")

    def cobble(self):
        print("Your shoe is as good as new!")
        self.condition = "New"