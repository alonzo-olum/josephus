#!/bin/env python3

def counting_sort(array):
    # initialize a counter size of distinct values
    lower_bound, upper_bound = min(array), max(array)
    counter = [0]*(upper_bound-lower_bound+1)
    # set the position of each item from min value referenced by occurrence
    for item in array:
        counter[item-lower_bound]+=1
    position = 0
    # set the actual position of the element
    for idx, item in enumerate(counter):
        num = idx + lower_bound
        for i in range(item):
            array[position] = num
            position += 1
    return array

# main block
from random import randrange

array = [randrange(1,9) for i in range(10)]
counting_sort(array)
print(array)
