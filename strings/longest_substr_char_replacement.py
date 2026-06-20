#!/bin/env python3

from collections import defaultdict

class Solution:
    def char_replacement(self, s, k):
        character_counts = defaultdict(int)

        window_start, max_win_size = 0, 0

        for i in range(len(s)):
            char = s[i]
            character_counts[char] += 1

            while self.get_replc(character_counts) > k:
                c = s[window_start]
                window_start += 1
                character_counts[c] -= 1

            max_win_size = max(max_win_size, i - window_start + 1)
        return max_win_size

    def get_max_entry(self, d):
        max_c, max_v = None, -float('inf')
        for key, val in d.items():
            if val > max_v:
                max_v = val
                max_c = key
        return (max_c, max_v)

    def get_replc(self, dicts):
        replc = 0
        max_c, _ = self.get_max_entry(dicts)
        for c, count in dicts.items():
            if c != max_c:
                replc += count
        return replc

# main block
sln = Solution()
strs = "ABABA"
k = 2
print(sln.char_replacement(strs, k))
