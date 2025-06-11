class Solution:
    def maxNumOfMarkedIndices(self, nums: List[int]) -> int:
        nums.sort()
        n=len(nums)
        ans=0
        j=int(n/2)
        for i in range(int(n/2)):
            while j<n and nums[i]*2>nums[j]:
                j+=1
            if j==n:
                break
            ans+=2
            j+=1
        return ans
