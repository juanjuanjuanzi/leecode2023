class Solution:
    def arrangeCoins(self, n: int) -> int:
        left=1
        right=n//2+1
        while left<right:
            mid=(left+right+1)>>1
            t=mid*(mid+1)//2
            if t<=n:
                left=mid
            else:
                right=mid-1
            
        return left
