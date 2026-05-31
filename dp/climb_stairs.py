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

# main block
if __name__ == '__main__':
    print(climbStairs(5))
