class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        for n in range(min(len(mat),len(mat[0]))):
            if self.squareexist(mat,n,threshold)==0:
              #说明边长小于等于n的都存在，而边长等于n+1的不存在
              #Squares exist for size ≤n, but not for n+1.
                return n
        return n+1
        #最大的正方形也存在
        #Squares exist up to the maximum size.

    def calSum(self,mat:List[List[int]],a:int,b:int,n:int)->int:
      """
      计算以（a，b）为左上角，边长为n的正方形内部所有数之和
      Calculate the sum of all numbers inside the square with top-left corner at (a, b) and side length n.
      """
        sum=0
        for i in range(n):
            for j in range(n):
                sum+=mat[a+i][b+j]
        return sum

    def squareexist(self,mat:List[List[int]],n:int,threshold:int)->int:
      """
      判断矩阵中是否存在边长为n+1的正方形内部所有数之和小于等于threshold，
      如果存在，return 1，反之，return 0.
      Determine whether there exists a square with side length n+1 in the matrix
      where the sum of all its internal numbers is less than or equal to the threshold.
      If such a square exists, return 1; otherwise, return 0.
      """
        for i in range(len(mat)-n):
            for j in range(len(mat[0])-n):
              #遍历所有可能的正方形
              #Traverse all possible squares in the matrix."
                if self.calSum(mat,i,j,n+1)<=threshold:
                  #注意这里的n是正方形边长-1
                  #Note that here, n is the side length of the square minus 1
                    return 1
                  #直接停止循环减少重复计算
                  #Break the loop prematurely to minimize repeated computations.
        return 0
# Runtime 3445ms
# Memory 21.84MB
