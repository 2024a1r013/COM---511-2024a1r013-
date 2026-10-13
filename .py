""""
wap to create a class which acts as calculator capable of finding square , cube and square root of a numberAA
""""
import math

class Calculator:

    def square(self, n):
        return n * n

    def cube(self, n):
        return n * n * n

    def square_root(self, n):
        return math.sqrt(n)


n = int(input("Enter a number: "))

c = Calculator()

print("Square:", c.square(n))
print("Cube:", c.cube(n))
print("Square Root:", c.square_root(n))