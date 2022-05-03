// this code is pretty stupid could wave off the laziness and write a function for swapping ughh python tuples are way better
void sortColors(int* nums, int numsSize){
    int low=0,mid=0,high=numsSize-1;
    while(mid <= high){
        if(nums[mid] == 0){
            int temp;
            temp = nums[low];
            nums[low] = nums[mid];
            nums[mid] = temp;
            low++;
            mid++;
        }
        else if(nums[mid] == 1){
            mid++;
        }
        else{
            int temp2;
            temp2 = nums[high];
            nums[high] = nums[mid];
            nums[mid] = temp2;
            high--;
        }
    }
}
