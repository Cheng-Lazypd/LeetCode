class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
      # 如果两个arr中的元素组成相同，那么一定可以通过相邻对调的方式把arr排成target，具体方式参考bubble sort
      # If the elements in target and arr are all the same, the arr can definitely be changed into the target by changing the position of two adjacent elements.
      # The method is the same as bubble sort.
        dic={}# 建立字典记录target中的元素组成  The dictionary records the elements in target.
        for i in range(len(target)):
            if target[i] not in dic:
                dic[target[i]]=1
            else:
                dic[target[i]]+=1
        for i in range(len(target)):
            if arr[i] not in dic:# arr中存在target中没有的元素  Some elements in arr DNE in target.
                return False
            else:
                dic[arr[i]]-=1
        for value in dic.values():
            if value!=0:# arr中存在某种元素其数量与target中同种元素数量不同  There exists a number in arr whose occuring times is different from the one in target.
                return False
        return True
# Run time 7ms
# Memory 18MB
