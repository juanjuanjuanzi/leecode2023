'''
执行用时：
60 ms
, 在所有 Python3 提交中击败了
80.16%
的用户
内存消耗：
19.5 MB
, 在所有 Python3 提交中击败了
10.57%
的用户
'''
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        cur=head
        init=ListNode(val=0,next=head)
        pre=init
        while cur:
            
            if cur.val==val:
                while cur and cur.val==val:
                    #print(cur)
                    cur=cur.next
                pre.next=cur
            if not cur:
                break
            pre=pre.next
            cur=cur.next
        return init.next
