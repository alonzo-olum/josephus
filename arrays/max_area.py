#!/bin/env python3

class Solution:
    def maxArea(self, height):
        left = [(0, height[0])]
        for i, n in enumerate(height):
            if n > left[-1][1]:
                left.append((i, n))
        right = [(len(height) - 1, height[len(height) - 1])]
        for i in range(len(height) - 1, -1, -1):
            n = height[i]
            if right[-1][1] < n:
                right.append((i, n))

        max_vol, l_index, r_index = 0, 0, 0
        while l_index < len(left) and r_index < len(right):
            l_ptr, l_h = left[l_index]
            r_ptr, r_h = right[r_index]

            curr_vol = min(l_h, r_h) * (r_ptr - l_ptr)
            max_vol  = max(curr_vol, max_vol)

            if r_index == len(right) - 1:
                l_index += 1
            elif l_index == len(left) - 1:
                r_index += 1
            elif l_h < r_h:
                l_index += 1
            else:
                r_index += 1
        return max_vol

    # original solution from:
    #https://github.com/jonahglover/Blind-75/blob/master/solutions/maxArea.py

# main block
if __name__ == '__main__':
    container_heights = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    a = s.maxArea(container_heights)
    print(a)
