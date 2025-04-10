class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        a=int(date1[0:4])-1
        b=int(date1[5:7])
        c=int(date1[8:10])
        if (a+1)%4==0 and ((a+1)%100!=0 or (a+1)%400==0):
            if b<=2:
                day1=a*365+a//4-a//100+a//400+(b-1)*31+c
            elif b>=3 and b<=8:
                day1=a*365+a//4-a//100+a//400+(b-1)*30-1+b//2+c
            else:
                day1=a*365+a//4-a//100+a//400+244+(b-9)*30+(b-9)//2+c
        else:
            if b<=2:
                day1=a*365+a//4-a//100+a//400+(b-1)*31+c
            elif b>=3 and b<=8:
                day1=a*365+a//4-a//100+a//400+(b-1)*30-2+b//2+c
            else:
                day1=a*365+a//4-a//100+a//400+243+(b-9)*30+(b-9)//2+c
        a=int(date2[0:4])-1
        b=int(date2[5:7])
        c=int(date2[8:10])
        if (a+1)%4==0 and ((a+1)%100!=0 or (a+1)%400==0):
            if b<=2:
                day2=a*365+a//4-a//100+a//400+(b-1)*31+c
            elif b>=3 and b<=8:
                day2=a*365+a//4-a//100+a//400+(b-1)*30-1+b//2+c
            else:
                day2=a*365+a//4-a//100+a//400+244+(b-9)*30+(b-9)//2+c
        else:
            if b<=2:
                day2=a*365+a//4-a//100+a//400+(b-1)*31+c
            elif b>=3 and b<=8:
                day2=a*365+a//4-a//100+a//400+(b-1)*30-2+b//2+c
            else:
                day2=a*365+a//4-a//100+a//400+243+(b-9)*30+(b-9)//2+c
        return abs(day1-day2)
# Runtime 0ms
# Memory 17.91MB
