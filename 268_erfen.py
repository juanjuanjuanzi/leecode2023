class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        total=int(n*(n+1)/2)
        count=0
        for v in nums:
            count+=v
        return total-count
