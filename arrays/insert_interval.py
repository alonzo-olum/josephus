#!/bin/env python3

class Solution:
    def insert(self, intervals, new):
        new_s, new_e = new
        res          = []
        inserted     = False
        for interv in intervals:
            s, e = interv
            if new_s <= s < new_e or\
                    new_s <= e < new_e or\
                    s < new_s and e > new_e:
                        new_s = min(new_s, s)
                        new_e = max(new_e, e)
            else:
                if not inserted and s > new_e:
                    res.append([new_s, new_e])
                    inserted = True
                res.append([s, e])
        if not inserted:
            res.append([new_s, new_e])
        
        return res
# main block
intervals = [[1, 4], [2, 5], [5, 7], [6, 10]]
new       = [3, 8]

sln       = Solution()
print(sln.insert(intervals, new))
