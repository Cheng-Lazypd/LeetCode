#include<stdio.h>


int min_length(int* nums,int numsSize, int num){
    int start=-1;
    int end=-1;
    for(int i=0;i<numsSize;i++){
        if(nums[i]==num){
            if(start==-1){
                start=i;
            }
            end=i;
        }
    }
    return end-start+1;
}

int findShortestSubArray(int* nums, int numsSize) {
    int time_max=0;
    int time[50000];
    for(int i=0;i<50000;i++){
        time[i]=0;
    }
    for (int i=0;i<numsSize;i++){
        time[nums[i]]++;
    }
    int num[50000];
    int j=0;
    for(int i=0;i<50000;i++){
        if(time[i]>time_max){
            time_max=time[i];
            j=0;
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
