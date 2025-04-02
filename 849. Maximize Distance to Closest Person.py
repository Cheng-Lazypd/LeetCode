class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        max=0
        length=0
        for i in range(len(seats)):
            if seats[i]==0:
                length+=1
            else:
                if length>max:
                    max=length
                length=0
        max=(max+1)//2
        if seats[0]==0:
            length=0
            for i in range(len(seats)):
                if seats[i]==0:
                    length+=1
                else:
                    break
            if length>max:
                max=length
        if seats[-1]==0:
            length=0
            for i in range(1,len(seats)+1):
                if seats[-i]==0:
                    length+=1
                else:
                    break
            if length>max:
                max=length
        return max
# Runtime 7ms
# Memory 18.45MB
