#!/usr/bin/env python3


def find_min_rotated(nums):

    if not nums: return None

    start, end = 0, len(nums) - 1

    while start <= end:
        if nums[start] <= nums[end]:
            return nums[start]

        mid = start + (end - start) // 2
        if nums[mid] < nums[mid - 1]:
            return nums[mid]

        if nums[mid] < nums[start]:
            end = mid - 1
        else:
            start = mid + 1

    raise 'Forbidden Path!'

# main block
if __name__ == '__main__':
    o = [ o for o in range(6)][1:]
    s = o[-3:]
    r = o[:-3]
    s.extend(r)

    print(find_min_rotated(s))
