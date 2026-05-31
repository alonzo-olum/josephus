#/bin/env python3

from collections import defaultdict


def threeSum(nums):
    seen, seen_count = set(), defaultdict(int)

    for i, val in enumerate(nums):
        if seen_count[val] >= 2:
            continue

        for val1 in nums[i+1:]:
            other_val = -(val1+val)
            val_tuple = tuple(sorted([val, val1, other_val]))
            if other_val in seen_count and seen_count[other_val] and val_tuple not in seen:
                seen.add(val_tuple)

        seen_count[val] += 1

    return [
            list(tup) 
            for tup in seen
            ]

# main block
if __name__ == '__main__':
    nums = [-1,0,1,2,-1,-4]
    res = threeSum(nums)
    print(res)
