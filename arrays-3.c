# https://leetcode.com/problems/sort-colors/
int removeDuplicates(int* nums, int numsSize){
    if(numsSize==0)
        return 0;
    int k = 0;
    for (int i = 1; i < numsSize; i++){
        if (nums[i] != nums[k]){
            nums[k + 1] = nums[i];
            k++;
            }
        }
    return k + 1;
}
