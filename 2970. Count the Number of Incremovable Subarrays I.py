class Solution:
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        n=len(nums)
        head=[nums[0]]#记录开头的严格增部分  record the strictly increasing part in the head
        end=[nums[-1]]#记录结尾的严格增部分  record the strictly increasing part in the end
        i=1
        while i<n and nums[i]>nums[i-1]:
            head.append(nums[i])
            i+=1
        i=-2
        while i>=-n and nums[i]<nums[i+1]:
            end=[nums[i]]+end
            i-=1
        a=len(head)
        b=len(end)
        if a==n:#原序列严格增  the original list in strictly increasing
            return int(n*(n+1)/2)
        ans=0
        for i in range(a):#去除子数列后包含头尾的情况  the case that contains both head and end
            for j in range(b):
                if head[i]<end[-j-1]:
                    ans+=1
        ans+=a+b+1#只包含头尾和空数列  the case that contains only head or end or an empty list
        return ans
#Run time 0ms
#Memory 17.8MB
