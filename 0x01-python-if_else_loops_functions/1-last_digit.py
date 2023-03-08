#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

print(f"Last digit of {number}", end=" ")

last = number % 10

if number < 0 and last != 0:
    print(f"is {(last - 10)}", end=" ")
else:
    print(f"is {last}", end=" ")

if (number < 0 or last < 6) and last != 0:
    print("and is less than 6 and not 0")
elif last > 5:
    print("and is greater than 5")
elif last == 0:
    print("and is 0")
