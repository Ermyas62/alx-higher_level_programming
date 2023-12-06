#!/usr/bin/python3
def uniq_add(my_list=[]):


    uniq = set(my_list)
    uniq_i = list(uniq)
    total = 0


    for i in uniq_i:
        total += i
        return total
