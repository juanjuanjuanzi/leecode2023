'''
执行用时：
68 ms
, 在所有 Python3 提交中击败了
18.94%
的用户
内存消耗：
20 MB
, 在所有 Python3 提交中击败了
5.11%
的用户
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur=head
        
        while cur:
            #print(cur.val)
            if cur.next and cur.next.val=="ok":
                return True
            cur.val="ok"
            cur=cur.next

        return False
      
'''
执行用时：
64 ms
, 在所有 Python3 提交中击败了
29.10%
的用户
内存消耗：
20.4 MB
, 在所有 Python3 提交中击败了
5.11%
的用户
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        seen = set()
        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False
      
'''
执行用时：
60 ms
, 在所有 Python3 提交中击败了
48.02%
的用户
内存消耗：
19.9 MB
, 在所有 Python3 提交中击败了
5.11%
的用户
'''
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next:
            return False
        
        slow = head
        fast = head.next

        while slow != fast:
            if not fast or not fast.next:
                return False
            slow = slow.next
            fast = fast.next.next
        
        return True

'''
执行用时：
56 ms
, 在所有 Python3 提交中击败了
69.85%
的用户
内存消耗：
20.1 MB
, 在所有 Python3 提交中击败了
5.11%
的用户
'''
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast is None:
                return False
            if fast == slow:
                return True
        return False
