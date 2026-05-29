#!/bin/env python3

def solution(arr):
    n = len(arr)
    max_len, curr_len = 2, 2
    
    for i in range(2, n):
       if arr[i] - arr[i-1] == arr[i-1] - arr[i-2]:
           curr_len += 1
       else:
           max_len = max(max_len, curr_len)
           curr_len = 2
    return max(max_len, curr_len)
# main block

if __name__ == '__main__':
    data = [3, 5, 7, 9, 11, 15, 19, 23, 27]
    print(solution(data))
