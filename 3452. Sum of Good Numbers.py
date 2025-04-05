class Solution:
    def sumOfGoodNumbers(self, nums: List[int], k: int) -> int:
        sum=0
        n=len(nums)
        for i in range(n):
            if (i-k<0 or nums[i-k]<nums[i]) and (i+k>=n or nums[i+k]<nums[i]):
                sum+=nums[i]
        return sum
# Runtime 3ms
# Memory 17.66MB
