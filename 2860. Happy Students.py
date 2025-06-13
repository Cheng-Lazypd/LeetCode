class Solution:
    def countWays(self, nums: List[int]) -> int:
        nums.sort()
        ans=0
        if nums[0]>0:
            ans+=1
        for i in range(1,len(nums)):
            if i <nums[i] and i>nums[i-1]:
                ans+=1
        if nums[-1]<len(nums):
            ans+=1
        return ans
