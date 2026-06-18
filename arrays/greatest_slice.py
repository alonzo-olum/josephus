#!/bin/env python3

def greatest_slice(seq):
    n = len(seq)
    return max((seq[i:j]
                for i in range(n)
                for j in range(i + 1, n + 1)
                ), key=sum)

# main block
seq = [1, 1, -1, 2, 0, -2]
print(greatest_slice(seq))
