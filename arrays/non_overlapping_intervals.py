#!/bin/env python3

class Solution:
    def non_overlapping(self, intervals):
        intervals.sort(key=lambda x: (x[1], -x[0]))
        s, e  = intervals[0]
        count = 0

        for interv in intervals[1:]:
            new_s, new_e = interv
            if new_s < e <= new_e:
                count += 1
                intervals.remove(interv)
            else:
                s, e = new_s, new_e
        return count

# main block
soln = Solution()
intervals = [
        [0,2],
        [1,3],
        [2,4],
        [3,5],
        [4,6]
        ]
intervals2 = [
        [-52,31],
        [-73,-26],
        [82,97],
        [-65,-11],
        [-62,-49],
        [95,99],
        [58,95],
        [-31,49],
        [66,98],
        [-63,2],
        [30,47],
        [-40,-26]
        ]
print(soln.non_overlapping(intervals2))
