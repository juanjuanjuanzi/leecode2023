#拓扑排序
class Solution(object):
    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        if n==1:
            return True
        if len(edges)<(n-1):
            return False
        dig=[0]*n
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
            dig[u]+=1
            dig[v]+=1

        #if 0 in dig and n>1:
        #    return False
        
        stack=deque()
        for i in range(n):
            if dig[i]==1:
                stack.append(i)
        cnt=0
        while stack:
            u=stack.popleft()
            cnt+=1
            for v in g[u]:
                dig[v]-=1
                if dig[v]==1:
                    stack.append(v)
        if cnt<n:
            return False
        return True
