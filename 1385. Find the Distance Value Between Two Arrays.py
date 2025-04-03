class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        ans=0
        for num1 in arr1:
            x=1
            for num2 in arr2:
                if abs(num1-num2)<=d:
                    x=0
            if x==1:
                ans+=1
        return ans
# Runtime 210ms
# Memory 17.9MB
