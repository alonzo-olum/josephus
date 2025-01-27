#!/bin/env python3

import itertools

from radix_sort import lsd, modulo

def radix_sort(array):
    digits = len(str(max(array)))

    for digit in range(digits):
        buckets = [[] for i in range(10)]
        for num in array:
            index = modulo(lsd(num, digit))
            buckets[index].append(num)
        array = list(itertools.chain(*buckets))
    return array

# main block
array = [112, 100, 230, 90, 104]
print(radix_sort(array))
