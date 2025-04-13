#!/bin/env python3

from binary_search import pivot, binary_search

class RotatedArray:

    def __init__(self, arr, k):
        self.arr = arr
        self.k = k

    @classmethod
    def rotate_arr(cls, arr, k):
        from collections import deque

        A = arr[:-k]
        B = deque(A)

        for i in reversed(arr[-k:]):
            B.appendleft(i)
        return cls(
                arr = list(B),
                k = k
                )

    def find_min_value(self):
        arr = self.arr
        low, high = 0, len(arr)-1
        pi = pivot(arr, low, high)                      # This step ensures that the rotated array marks the search range starting from lowest point (pivot)

        if arr[pi] == arr[self.k]:                      # pivot marks the first element right of inflection pount
            return pi
        if pi == 0:                                     # first element is the pivot rotation at 0 (no rotation)
            return binary_search(arr, low, high, self.k)
        if arr[0] <= arr[self.k]:                       # self proof condition abit redundant
            return binary_search(arr, low, pi-1, self.k)
        return binary_search(arr, pi+1, high, self.k)


if __name__ == '__main__':
    arr = [0, 1, 2, 4, 5, 6, 7]
    k = 4
    rotated_arr = RotatedArray.rotate_arr(arr, k)
    index = rotated_arr.find_min_value()
    print(rotated_arr.arr[index])
