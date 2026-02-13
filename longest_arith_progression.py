#!/bin/env python3

def longest_arith_progression(arr):
    n = len(arr)

    # Base Case for list with a single item
    if n <= 1:
        return n

    # Initialize an adjacent list of map in format:
    # [
    #   { diff: count },
    #   ...
    # ]
    dp = [{} for _ in range(n)]
    max_len = 2
    # It seems like straight O(n^2) runtime
    # But the iteration is actually: O(n(n-1))
    for u in range(n):
        for v in range(u):
            diff = arr[u] - arr[v]
            dp[u][diff] = dp[v].get(diff, 1) + 1
            max_len = max(max_len, dp[u][diff])
    return max_len

if __name__ == '__main__':
    seq = [4, 2, 1, 7, 5, 10, 9]
    print(longest_arith_progression(seq))
