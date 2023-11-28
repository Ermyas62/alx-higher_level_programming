#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0:
        L_digit = number % 10
    else:
        L_digit = number % -10
        L_digit *= -1

    print("{:d}".format(L_digit), end='')
    return (L_digit)
