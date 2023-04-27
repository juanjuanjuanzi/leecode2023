'''
执行用时：88 ms, 在所有 Python3 提交中击败了5.73%的用户
内存消耗：15.1 MB, 在所有 Python3 提交中击败了20.25%的用户
'''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        x1=set(nums1)
        x2=set(nums2)
        temp=x1&x2
        ans=[]
        for v in temp:
            ans+=[v]*min(nums1.count(v),nums2.count(v))

        return ans
      
      
 '''
 哈希表
 95%
 56%
 '''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) > len(nums2):
            return self.intersect(nums2, nums1)
        
        m = collections.Counter()
        for num in nums1:
            m[num] += 1
        
        intersection = list()
        for num in nums2:
            if (count := m.get(num, 0)) > 0:
                intersection.append(num)
                m[num] -= 1
                if m[num] == 0:
                    m.pop(num)
        
        return intersection
      
      
 '''
 83%
 27.7%
 排序 + 双指针
 '''
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()

        length1, length2 = len(nums1), len(nums2)
        intersection = list()
        index1 = index2 = 0
        while index1 < length1 and index2 < length2:
            if nums1[index1] < nums2[index2]:
                index1 += 1
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                intersection.append(nums1[index1])
                index1 += 1
                index2 += 1
        
        return intersection
