# Dutch National Flag problem
# https://leetcode.com/problems/sort-colors
# low,mid,high = 0,0,len(arr)-1
# if arr[mid] equals to 0 then arr[low] and arr[mid] are swapped and mid,low pointers are incremented
# if arr[mid] equals to 1 no swapping only mid pointer is incremented
# if arr[mid] equals to 2 arr[high] and arr[mid] are swapped and high pointer is incremented
def sortColors(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """ 
        low = 0 
        high = len(arr) - 1 
        mid = 0 
        while mid <= high: 
            if arr[mid] == 0: 
                arr[low],arr[mid] = arr[mid],arr[low] 
                low = low + 1 
                mid = mid + 1 
            elif arr[mid] == 1: 
                mid = mid + 1 
            else: 
                arr[mid],arr[high] = arr[high],arr[mid] 
                high = high - 1 
