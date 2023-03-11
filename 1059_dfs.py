class Solution(object):
    def leadsToDestination(self, n, edges, source, destination):
        """
        :type n: int
        :type edges: List[List[int]]
        :type source: int
        :type destination: int
        :rtype: bool
        """
        #采用dfs
        #访问的叶子节点只能为destination,且访问路径中无环
        vis=[0]*n
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)

        valid=[True]

        def dfs(i):
            vis[i]=1
            if valid[0]==False:
                return
            if len(g[i])==0 and i!=destination:
                valid[0]=False
                return
            for v in g[i]:
                if vis[v]==1:
                    valid[0]=False
                    return 
                if vis[v]==0:
                    dfs(v)
            vis[i]=2

        dfs(source)
        return True if valid[0] else False
