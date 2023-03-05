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
        vis=[0]*n
        father={}
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        valid=[1]  
        def dfs(u):
            if not valid[0]:
                return
            vis[u]=1
            for v in g[u]:
                if not valid[0]:
                    return
                #print(father,vis,u,v,valid[0])
                if vis[v]==0:
                    father[v]=u
                    dfs(v)
                elif vis[v]==1 and father[u]!=v:
                    valid[0]=0
                    father[v]=u
                    #print('ok')
                    return                
            vis[u]=2

        for i in range(n):
            if not valid[0]:
                return False
            if vis[i]==0:
                dfs(i)
        
        return True
