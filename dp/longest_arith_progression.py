#!/bin/env python3

def longest_arith_subsequence(arr):
    n, max_len  = len(arr), 2
    if n <= 1:
        return n
    # dp is a [ { diff: length of subsequence ending at i}, ... ]
    dp = [
            {}
            for _ in range(n)
            ]

    for u in range(n):
        for v in range(u):
            diff = abs(arr[u] - arr[v])
            dp[u][diff] = dp[v].get(diff, 1) + 1
            max_len = max(max_len, dp[u][diff])
    return max_len

# Example Usage
if __name__ == '__main__':
    arr1 = [3, 4, 5, 2, 10, 7, 9, 13, 11]
    arr2 = [100, 4, 200, 1, 3, 2]
    print(longest_arith_subsequence(arr2))
