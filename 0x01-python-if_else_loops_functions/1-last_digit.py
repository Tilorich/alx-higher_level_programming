#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
number = str(number)
figure = int(number[-1])
if figure > 5:
    print(f"Last digit of {number} is {figure} and is greater than 5")
elif figure < 6:
    if figure > 0:
      print(f"Last digit of {number} is {figure} and is less than 6 and not 0")
    else:
      print(f"Last digit of {number} is {figure} and is 0")
