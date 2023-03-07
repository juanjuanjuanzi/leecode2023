class Solution(object):
    def sequenceReconstruction(self, nums, sequences):
        """
        :type nums: List[int]
        :type sequences: List[List[int]]
        :rtype: bool
        """
        n=len(nums)
        ind=[0]*n
        
        g=[[] for _ in range(n)]
        #init graph
        for seq in sequences:
            for i in range(len(seq)-1):
                u=seq[i]
                v=seq[i+1]
                if (v-1) in g[u-1]:
                    continue
                g[u-1].append(v-1)
                ind[v-1]+=1
       
        #仅存在一条路径可以遍历完所有节点,没有杂支
        q=deque()
        for x in range(n):
            if ind[x]==0:
                q.append(x)
        while q:
            if len(q)>1:
                return False
            u=q.popleft()
            for v in g[u]:
                ind[v]-=1
                if ind[v]==0:
                    q.append(v)
        return True
