#!/usr/bin/python3
from models.rectangle import Rectangle

if __name__ == "__main__":
    r1 = Rectangle(10, 2, 1, 9)
    print(r1)
    r1_dict = r1.to_dictionary()
    print(r1_dict)
    print(type(r1_dict))

    r2 = Rectangle(1, 1)
    print(r2)
    r2.update(**r1_dict)
    print(r2)
    print(r2 == r1)
