#!/usr/bin/python3
for number in range(100):
    if number == 89:
        print(number)
    if (number // 10) == (number % 10):
        continue
    elif (number // 10) > (number % 10):
        continue
    print("{:0>2}, ".format(number), end='')
