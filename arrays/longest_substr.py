#!/bin/env python3

class Solution:
    def longest_substr(self, s):
        if not s: return 0
        max_len, start = -1, 0
        char_count     = dict()

        for i, char in enumerate(s):
            if char_count.get(char) != None:
                start = max(start, char_count[char] + 1)

            char_count[char] = i
            max_len = max(max_len, i - start + 1)
        return max_len
# main block
sln = Solution()
s   = "abcad"
print(sln.longest_substr(s))
