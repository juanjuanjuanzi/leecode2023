class Solution(object):
    def distanceToCycle(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #就是判断哪些点在环里
        #在环里的节点为0
        g=defaultdict(set)
        circle=set()
        #roots=set()
        degree=[0]*n
        for x,y in edges:
            g[x].add(y)
            g[y].add(x)
            degree[x]+=1
            degree[y]+=1
        q=[]
        dis=[float('inf')]*n#由环中的每个点出发，到其他点的最短距离，不断更新
        circle=[]
        other=set()
        for i in range(n):
            if degree[i]==1:
                q.append(i)
                other.add(i)
        while q:
            x=q.pop(0)
            for y in g[x]:
                degree[y]-=1
                if degree[y]==1:
                    q.append(y)
                    other.add(y)

        circle=set([i for i in range(n)])-other
        for i in circle:
            dis[i]=0

        for i in circle:
            q=[i]
            while q:
                x=q.pop(0)
                for y in g[x]:
                    if y not in circle and dis[y]>dis[x]+1:
                        dis[y]=dis[x]+1
                        q.append(y)
        return dis
