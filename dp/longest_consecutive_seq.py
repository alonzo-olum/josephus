
class Solution:
    def longest_consecutive_seq(self, nums):
        nodes = {}
        for n in nums:
            if n not in nodes:
                nodes[n] = False
            if n - 1 in nodes:
                nodes[n - 1] = True
            if n + 1 in nodes:
                nodes[n + 1] = True

        sources = []
        for n, has_inbound in nodes.items():
            if not has_inbound:
                sources.append(n)
        max_run  = 0
        for n in sources:
            curr_run = 1
            while (n + curr_run) in nodes:
                curr_run += 1
            max_run = max(max_run, curr_run)
        return max_run

# main block
sln = Solution()
seq = [3, 6, 1, 5, 8, 7]
print(sln.longest_consecutive_seq(seq))
