#!/usr/bin/python3
"""1-main"""
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 2)
    print(r1.id)
    print(r1.width)
    print(r1.height)

    r2 = Rectangle(2, 10)
    print(r2.id)
    print(r2.width)
    print(r2.height)

    r3 = Rectangle(10, 2, 0, 0, 12)
    print(r3.id)
    print(r3.width)
    print(r3.height)
