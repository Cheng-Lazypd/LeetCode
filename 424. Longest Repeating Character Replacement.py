class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans=0
        for i in range(65,91):
            a=self.longrepeat(self.trans(s,chr(i)),k)
            if a>ans:
                ans=a
        return ans 

    def longrepeat(self,lis:List[int],k:int)->int:
        max_sum=0
        for i in range(len(lis)):
            if i%2==1:
                a=0
                for j in range(i-1):
                    a+=lis[j]
                sum=0
                sum0=lis[i]
                while sum0<=k and i+1<len(lis):
                    sum+=lis[i]+lis[i-1]
                    i+=2
                    sum0+=lis[i]
                sum+=lis[i-1]+lis[i]-max((sum0-k),-a)
                if sum>max_sum:
                    max_sum=sum
        return max_sum
    
    def trans(self,s:str,char:str)->List[int]:
        x=1
        ans=[0]
        for cha in s:
            if x==1:
                if cha==char:
                    ans[-1]+=1
                else:
                    x=0
                    ans.append(1)
            else:
                if cha==char:
                    x=1
                    ans.append(1)
                else:
                    ans[-1]+=1
        if x==1:
            ans.append(0)
        return ans
