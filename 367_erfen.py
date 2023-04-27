class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left=1
        right=num
        while left<right:
            mid=(left+right)>>1
            
                
            if mid*mid>num:
                right=mid-1
            elif mid*mid<num:
                left=mid+1
            else:
                return True
        #print(left)
        if left*left==num or (left+1)*(left+1)==num:# or (left-1)*(left-1)==num:
            return True
        else:
            return False
