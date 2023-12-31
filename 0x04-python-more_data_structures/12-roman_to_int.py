#!/usr/bin/python3
def roman_to_int(roman_string):
    romans = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000,
              'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    num = 0

    if roman_string is None or type(roman_string) is not str:
        return (0)
    for i in range(len(roman_string)):
        if i > 0 and romans[roman_string[i]] > romans[roman_string[i - 1]]:
            num += romans[roman_string[i]] - 2 * romans[roman_string[i - 1]]
        else:
            num += romans[roman_string[i]]
    return num
