#!/bin/env python3

# The main difference between This problem: Longest Subarray
# and Longest Subsequence (Longest Arithmetic Progression)
# is that this particular problem requires a contigous subarray

def longest_subarray(seq):

    n = len(seq)
    max_len, curr_len, start, max_start = 1, 1, 0, 0

    for i in range(1, n):
        if i == 1:
            diff = seq[i] - seq[i-1]
            curr_len = 2
        else:
            if seq[i] - seq[i-1] == diff:
                curr_len += 1
            else:
                diff = seq[i] - seq[i-1]
                curr_len = 2
                start = i - 1
            if curr_len > max_len:
                max_len = curr_len
                max_start = start
    return seq[max_start:max_start + max_len]

# main block

if __name__ == '__main__':

    seq = [2, 6, 5, 1, 9]
    print(longest_subarray(seq))
