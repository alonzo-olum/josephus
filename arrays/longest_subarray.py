#!/bin/env python3

def solution(arr):
    n = len(arr)
    max_len, curr_len, start_index, max_start = 1, 1, 0, 0

    for i in range(1, n):
        if i == 1:
            diff = arr[1] - arr[0]
            curr_len = 2
        else:
            if arr[i] - arr[i-1] == diff:
                curr_len += 1
            else:
                diff = arr[i] - arr[i-1]
                curr_len = 2
                start_index = i-1
            if curr_len > max_len:
                max_len = curr_len
                max_start = start_index
    return arr[max_start:max_start + max_len]
# main block
if __name__ == '__main__':
    arr0 = [6, 3, 5, 7, 9]
    arr1 = [3, 4, 5, 2, 10, 7, 9, 13, 11]
    arr2 = [8, 4, 1, 2, 5, 7, 9, 13, 11]
    print(solution(arr2))
