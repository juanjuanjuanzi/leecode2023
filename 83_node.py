# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        total=[head.val]
        pre=head
        cur=head.next
        while cur:
            if cur.val in total:
                pre.next=cur.next
            else:
                total.append(cur.val)
                pre=pre.next
            cur=cur.next
        return head 
      
      
'''
执行用时：
40 ms
, 在所有 Python3 提交中击败了
82.73%
的用户
内存消耗：
16.2 MB
, 在所有 Python3 提交中击败了
5.20%
的用户
'''
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        while p and p.next:
            if p.val==p.next.val:
                p.next=p.next.next
                continue
            p=p.next
        return head
