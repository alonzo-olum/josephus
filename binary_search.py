#!/bin/env python3
    
def binary_search(arr, low, high, key):
        while low <= high:
            mid = low + (high-low)//2
            if arr[mid] == arr[key]:
                return mid
            if arr[mid] > arr[key]:
                high = mid - 1
            else:
                low = mid + 1
        return -1

def pivot(arr, low, high):
        while low < high:
            if arr[low] <= arr[high]:
                return low
            mid = (low+high)//2

            if arr[mid] > arr[high]:
                low = mid+1
            else:
                high = mid
        return low

