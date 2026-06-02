#!/bin/env python3

class Solution:
    def best_buy_sell(self, prices):
        max_profit = 0
        best_buy, best_sell = prices[:1][0], prices[:1][0]

        for p in prices:
            if p > best_sell:
                best_sell  = p
                max_profit = max(max_profit, best_sell - best_buy)
            if p < best_buy:
                best_buy  = p
                best_sell = p
        return max_profit

# main block
if __name__ == '__main__':
    s      = Solution()
    profit = s.best_buy_sell([7, 1, 3, 4, 8])
    
    print(profit)
