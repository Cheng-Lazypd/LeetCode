#include<stdio.h>


int min_length(int* nums,int numsSize, int num){
    //This is a helper function.
    //这个函数计算在nums里，包含所有num的最小连续部分的长度
    //This function calculate the length of the smallest possible length 
    //of the (contiguous) subarray of nums that contains all the num in nums.
    int start=-1;
    int end=-1;
    for(int i=0;i<numsSize;i++){
        if(nums[i]==num){
            if(start==-1){//找到nums中第一个num    find the first num in nums
                start=i;
            }
            end=i;//每次遇到一个新的num，同步更新一次end    Whenever we come across a new num in nums, we update the end.
        }
    }
    return end-start+1;
}

int findShortestSubArray(int* nums, int numsSize) {
    //Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.
    //Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
    int time_max=0;
    int time[50000];//这个array记录了每个正整数在nums里出现的次数    This array counts the times each positive int appears in nums.
    for(int i=0;i<50000;i++){
        time[i]=0;//初始化    initialize time
    }
    for (int i=0;i<numsSize;i++){
        time[nums[i]]++;
    }
    int num[50000];//这个array包含拥有最大出现次数的所有num    This array contains all the num with the largest time.
    int j=0;//同时作为num的更新index，也是num的长度    j stands for the index of the updating of num and the length of num.
    for(int i=0;i<50000;i++){
        if(time[i]>time_max){
            time_max=time[i];
            j=0;//重置num    reset num
            num[j]=i;
        }
        if(time[i]==time_max){
            j++;
            num[j]=i;
        }
    }
    int min_leng=50000;
    int length=0;
    for(int i=0; i<=j;i++){
        length=min_length(nums,numsSize,num[i]);
        if(length<min_leng){
            min_leng=length;
        }
    }
    return min_leng;
}
//Runtime 70ms
//Memory 10.53MB
