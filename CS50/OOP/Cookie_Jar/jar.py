import sys

class Jar:
    def __init__(self, capacity=12):
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Invalid capacity")
        self.cookies = 0

    def __str__(self):
        return f"Cookie "*self.cookies

    def deposit(self, n):
        if n + self.cookies <= self.capacity:
            self.cookies += n
        else:
            raise ValueError("Exceeding capacity")

    def withdraw(self, n):
        if self.cookies >= n:
            self.cookies -= n
        else:
            raise ValueError("Not enough cookies in jar")

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self.cookies
    
jar = Jar()
