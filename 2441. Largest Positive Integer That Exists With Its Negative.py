class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        max=-1
        for num in nums:
            if -num in nums:
                if max<num:
                    max=num
        return max
# Run time 125ms
# Memory 17.9MB
