class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
      """
      Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
      Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
      """
        value=[]#记录数值  record the value in num
        time=[]#记录数值出现的次数  record the time that certain value appears in num
        for i in range(len(nums)):
            if nums[i] in value:
                time[value.index(nums[i])]+=1
            else:
                value.append(nums[i])
                time.append(1)
        maxtime=0
        length=0
        minlength=50000
        for i in range(len(time)):
            if time[i]>maxtime:
                maxtime=time[i]#找到最大出现次数  find maxtime
        for i in range(len(time)):
            if time[i]==maxtime:
                start=-1
                end=-1
                for j in range(len(nums)):#找到最小长度  find minlength
                    if nums[j]==value[i]:
                        if start==-1:
                            start=j
                        end=j
                length=end-start+1
                if length<minlength:
                    minlength=length
        return minlength
