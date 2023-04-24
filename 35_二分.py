class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            mid=(left+right)>>1
            if(nums[mid]==target):
                return mid
            elif nums[mid]>target:
                right=mid-1
            elif nums[mid]<target:
                left=mid+1
        if nums[left]<target:
            return left+1
        else:
            return left
