#!/usr/bin/python
def no_c(my_string):
    # Write a function that removes all characters c and C from a string
    new_string = my_string.translate({ord(i): None for i in "cC"})
    return (new_string)
