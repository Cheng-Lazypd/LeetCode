class Solution:
    def longestSemiRepetitiveSubstring(self, s: str) -> int:
        ans=0
        x=0
        l=1
        i=0
        while i<len(s)-1:
            if s[i]==s[i+1]:
                if x==1:
                    ans=max(ans,l)
                    x=0
                    l=1
                    i=j
                else:
                    x=1
                    l+=1
                    i+=1
                    j=i
            else:
                l+=1
                i+=1
        return max(ans,l)
