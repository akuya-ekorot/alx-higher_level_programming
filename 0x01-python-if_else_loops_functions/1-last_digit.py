#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print(f"Last digit of {number}", end=" ")

if number > 0:
    last = number % 10
else:
    number *= -1
    last = number % 10

print(f"is {last}", end=" ")

if last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")