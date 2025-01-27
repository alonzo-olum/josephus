#!/bin/env python3

def longest_substring(chars):
    char_map = {}
    start, max_len = 0, 0
    for idx, ch in enumerate(chars):
        if ch in char_map and char_map[ch] >= start:
            start = char_map[ch] + 1
        else:
            max_len = max(max_len, idx - start + 1)
        char_map[ch] = idx
    print("longest_substring: %d, %s" % (max_len, char_map))
 # Main block
strs = "abcabcbb"
longest_substring(strs)
