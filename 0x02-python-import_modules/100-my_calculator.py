#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, mul, div
    operator = ['+', '-', '*', '/']
    if len(sys.argv) - 1 != 3:
        print("Usage: .//100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == operator[0]:
        print("{} {} {} = {}".format(a, operator[0], b, add(a, b)))
    elif sys.argv[2] == operator[1]:
        print("{} {} {} = {}".format(a, operator[1], b, sub(a, b)))
    elif sys.argv[2] == operator[2]:
        print("{} {} {} = {}".format(a, operator[2], b, div(a, b)))
    elif sys.argv[2] == operator[3]:
        print("{} {} {} = {}".format(a, operator[3]. b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
