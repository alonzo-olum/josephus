#!/usr/bin/env python3

def climb_stairs(n):
    if n < 2:
        return 1

    prev, curr = 1, 2
    for i in range(3, n+1):
        ne = curr + prev
        prev = curr
        curr = ne
    return curr

def climb_stairs_dp(n):
    dp    = [0] * n
    dp[0] = 1
    dp[1] = 2

    for i in range(2, n):
        dp[i] = dp[i - 1] + dp[i - 2];
    return dp[n - 1]


# main block
if __name__ == '__main__':
    print(climb_stairs_dp(5))
