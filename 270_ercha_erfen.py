# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        
        if root.val==target:
            #print(root.val, target)
            return root.val
        
        ans=root.val
        while root:
            ans=min(root.val, ans,key=lambda x: abs(target-x))
            root=root.left if root.val>target else root.right
        return ans
