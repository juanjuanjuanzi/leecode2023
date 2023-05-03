'''
8.63
23.37
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head   
        cur=head.next
        head.next=None
        pre=head
        
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp

        return pre
      
'''
94.97
23.82
'''
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:        
        pre=None
        cur=head
        
        while cur:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp

        return pre
