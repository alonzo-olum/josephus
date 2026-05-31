#!/usr/bin/env python3

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])

    merge = [intervals[0]]

    for current in intervals[1:]:
        last = merge[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merge.append(current)
    return merge

# main block

intervals = [[1,3], [2,6], [8,10], [15,18]]
print("[merge_intervals] %s\n" % (merge_intervals(intervals)))
