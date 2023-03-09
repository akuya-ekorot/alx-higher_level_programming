#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    if len(argv) != 4:
        exit("Usage: {} <a> <operator> <b>".format(argv[0]))
    left = int(argv[1])
    op = argv[2]
    right = int(argv[3])

    if op == "+":
        calc = add(left, right)
    elif op == "-":
        calc = sub(left, right)
    elif op == "*":
        calc = mul(left, right)
    elif op == "/":
        calc = div(left, right)
    else:
        exit("Unkown operator. Available operators: +, -, * and /")

    print("{} {} {} = {}".format(left, op, right, calc))
