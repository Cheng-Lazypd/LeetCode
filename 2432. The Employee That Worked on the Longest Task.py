class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        max=logs[0][1]
        ans=logs[0][0]
        for i in range(1,len(logs)):
            if logs[i][1]-logs[i-1][1]>max:
                ans=logs[i][0]
                max=logs[i][1]-logs[i-1][1]
            elif logs[i][1]-logs[i-1][1]==max:
                if ans>logs[i][0]:
                    ans=logs[i][0]
        return ans
#Run time 11ms
#Memory 18.1MB
