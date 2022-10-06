#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if number % 3 and number % 5:
            print("FizzBuzz ", end='')
        elif number % 5:
            print("Buzz ", end='')
        elif number % 3:
            print("Fizz ", end='')
        else:
            print("{} ".format(number), end='')
