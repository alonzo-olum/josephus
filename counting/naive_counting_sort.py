#!/bin/env python3

def counting_sort(arr, exp):
    n = len(arr)
    count, output = [0]*n, [0]*10
    for u in range(n):
        index = (arr[u]//exp) % 10
        count[index] += 1
    for u in range(1, 10):
        count[u] += count[u - 1]

    u = n - 1
    while u >= 0:
        index = (arr[u]//exp) % 10
        output[count[index] - 1] = arr[u]
        count[index] -= 1
        u -= 1

    for u in range(n):
        arr[u] = output[u]
