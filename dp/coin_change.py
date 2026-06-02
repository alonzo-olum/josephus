#!/bin/env python3

def coin_change(coins, amt):
    coins.sort()
    dp    = [-1] * (amt + 1)
    dp[0] = 0

    for curr in range(1, amt + 1):
        subtotal_no = float('inf')
        for c in coins:
            coin_subtotal = curr - c
            if coin_subtotal < 0:
                break
            if dp[coin_subtotal] >= 0:
                subtotal_no = min(subtotal_no, dp[coin_subtotal])
        if subtotal_no < float('inf'):
            dp[curr] = subtotal_no + 1
    return dp[amt]

# main block
if __name__ == '__main__':
    coins = [1, 2, 5]
    amt = 11

    print(coin_change(coins, 11))
