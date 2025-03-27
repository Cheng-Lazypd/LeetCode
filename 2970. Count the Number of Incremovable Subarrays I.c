int incremovableSubarrayCount(int* nums, int numsSize) {
    int a=1;//开头严格增的序列长度  the length of the strictly increasing part at the head
    int b=1;//结尾严格增的序列长度  the length of the strictly increasing part at the end
    while(a<numsSize && nums[a-1]<nums[a]){
        a++;
    }
    while(b<numsSize && nums[numsSize-b]>nums[numsSize-b-1]){
        b++;
    }
    if(a==numsSize){//原序列严格增的情况  the original array is strictly increasing
        return a*(a+1)/2;
    }
    int ans=0;
    for(int i=0;i<a;i++){
        for (int j=0;j<b;j++){
            if (nums[i]<nums[numsSize-j-1]){
                ans++;//包含头尾的情况  the case that contains both the head and the end
            }
        }
    }
    ans+=a+b+1;//包含头或尾的情况以及空序列的情况  the case the contains only the head or the end or the empty array
    return ans;
}
//Runtime 0ms
//Memory 8.9MB
