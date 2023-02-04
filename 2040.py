class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: int
        """
        ans=[]
        for i in nums1:
            for j in nums2:
                ans.append(nums1[i]*nums2[j])

        ans.sort()
        return ans[k-1]
