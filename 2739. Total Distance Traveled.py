class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        if (additionalTank*4+1)<=mainTank:
            return 10*(additionalTank+mainTank)
        return 10*mainTank+10*((mainTank-1)//4)
# Run time 3ms
# Memory 17.86MB
