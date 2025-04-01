class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones)==2:
            return stones[1]-stones[0]
        max=0
        for i in range(len(stones)-2):
            if max<abs(stones[i+2]-stones[i]):
                max=abs(stones[i+2]-stones[i])
        return max
# Run time 19ms
# 32.8MB
