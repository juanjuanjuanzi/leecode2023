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
        
'''
执行用时：
28 ms
, 在所有 Python3 提交中击败了
96.37%
的用户
内存消耗：
14.8 MB
, 在所有 Python3 提交中击败了
82.75%
的用户
'''
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        left=1
        right=num//2+1
        while left<=right:
            mid=(left+right)>>1
                           
            if mid*mid>num:
                right=mid-1
            elif mid*mid<num:
                left=mid+1
            else:
                return True

        '''
        if left*left==num or (left+1)*(left+1)==num:# or (left-1)*(left-1)==num:
            return True
        else:
            return False
        '''
        return False
    
'''
执行用时：
28 ms
, 在所有 Python3 提交中击败了
96.46%
的用户
内存消耗：
14.9 MB
, 在所有 Python3 提交中击败了
22.33%
的用户
'''
class Solution:
    def guessNumber(self, n: int) -> int:
        left=1
        right=n
        while left < right:
            mid=(left + right)>>1
            
            if guess(mid)<=0:
                right=mid                
            else:
                left=mid+1
        
        return left
        
