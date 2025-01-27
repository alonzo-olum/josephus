#!/usr/bin/env python3

import heapq

def kth_largest(nums, k):
    # initialize a minimum heap, first k-elements
    heap = nums[:k]
    heapq.heapify(heap)

    for num in nums[k:]:
        print("num: %d, heap[0]: %d" % (num, heap[0]))
        # current gt min root,
        # replace it iteratively with min of largest remnants
        if num > heap[0]:
            heapq.heapreplace(heap, num)
    return heapq.heappop(heap)

# main block
nums = [3,2,1,4,5,6]
k=3
print("The Kth largest element is {}".format(kth_largest(nums, k)))
