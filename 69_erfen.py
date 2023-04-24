class Solution:
    def mySqrt(self, x: int) -> int:
        left=0
        right=46340
        while left<right:
            mid=(left+right)>>1
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1
        if left*left<=x:
            return left
        else:
            return left-1
