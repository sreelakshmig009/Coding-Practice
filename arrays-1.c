// https://leetcode.com/problems/find-the-duplicate-number/submissions/
int findDuplicate(int* nums, int numsSize){
    int* count = calloc(sizeof(int),numsSize);
    for(int i=0;i<numsSize;i++){
        count[nums[i]]++;
        if(count[nums[i]]>1)
            return nums[i];
    }
    return -1;
}
