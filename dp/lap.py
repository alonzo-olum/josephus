#!/bin/env python3

class LAP:
    def longest_consecutive(self, nums):
        nodes = {}
        for n in nums:
            if n not in nodes:
                nodes[n] = False
            if n - 1 in nodes:
                nodes[n] = True
            if n + 1 in nodes:
                nodes[n + 1] = True
        sources = []
        for n, has_inbound in nodes.items():
            if not has_inbound:
                sources.append(n)

        max_run = 0
        for n in sources:
            curr = 1
            while (n + curr) in nodes:
                curr += 1
            max_run = max(curr, max_run)
        return max_run
# Example Usage
if __name__ == '__main__':
    arr1 = [3, 4, 5, 2, 10, 7, 9, 13, 11]
    arr2 = [100, 4, 200, 1, 3, 2]
    l = LAP()
    print(l.longest_consecutive(arr2))

