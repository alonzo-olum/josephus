#!/usr/bin/env python3

class Kadane:
    def __init__(self, arr):
        self.arr =  arr

    def max_subarray(self):
        max_sum = self.arr[0]
        curr_sum = self.arr[0]
        for num in self.arr[1:]:
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)
        print("max_subarray: %d" % (max_sum))

# main block
if __name__ == '__main__':
    k = Kadane([1,4,1,-2,3,5,-6])
    k.max_subarray()

