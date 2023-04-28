'''
执行用时：
144 ms
, 在所有 Python3 提交中击败了
54.25%
的用户
内存消耗：
33.8 MB
, 在所有 Python3 提交中击败了
5.00%
的用户
'''
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        seen=set()
        cura=headA
        curb=headB
        while cura or curb:
            if cura:
                if cura in seen:
                    return cura
                else:
                    seen.add(cura)
                cura=cura.next
            if curb:
                if curb in seen:
                    return curb
                else:
                    seen.add(curb)
                curb=curb.next
        return None
