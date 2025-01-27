#!/bin/env python3

def radix_sort(array):
    digits, size = len(str(max(array))), len(array)
    for digit in range(digits):
        counter, sort_array = [0]*10, [0]*size
        for num in array:
            idx = modulo(lsd(num, digit))
            counter[idx] += 1
            print("[counter]: %s" % (counter))

        for i in range(1,10):
            counter[i] += counter[i-1]
            print("[counter2]: %s" % (counter))

        i = size-1
        while i >= 0:
            idx = modulo(lsd(array[i], digit))
            sort_array[counter[idx]-1] = array[i]
            print("[sorted]: %s" % (sort_array))
            counter[idx] -= 1
            print("[counter3]: %s" % (counter))

            i -= 1
        array = sort_array
    return array

# least significant digit
def lsd(number, digit):
    return number//(10**digit)

def modulo(digit): return digit % 10
