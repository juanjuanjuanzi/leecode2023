class Solution(object):
    def mostSimilar(self, n, roads, names, targetPath):
        """
        :type n: int
        :type roads: List[List[int]]
        :type names: List[str]
        :type targetPath: List[str]
        :rtype: List[int]
        """
        #init graph
        g=defaultdict(list)
        for u,v in roads:
            g[u].append(v)
            g[v].append(u)
	    # two memo
	    m=len(targetPath)
	    dis=[[float('inf')]*n for _ in range(m)]
        pre=[[-1]*n for _ in range(m)]

        map={}      
        for i in range(n):
            map[i]=names[i]
        #初始化i=0时从各个顶点出发的cost情况:
        for j in range(n):
            if map[j]==targetPath[0]:
                dis[0][j]=0
            else:
                dis[0][j]=1
            

        for i in range(1,m):
            #在每一层中，逐个为每个start的选择更新对应的dis和bestnext
            #因此开始选择不同起始点的行为，生成了n颗子树
            for j in range(n):
                cost=0
                if map[j]!=targetPath[i]:
                    cost=1
                #为上一层每个节点的所有分支中，距离最小的分支，并更新
                for k in g[j]:
                    
                    curr=cost+dis[i-1][k]
                    if curr<dis[i][j]:
                        dis[i][j]=curr
                        pre[i][j]=k
        #print(dis)
        #print(pre)
        mincost=float('inf')
        end=0
        #看dis[m-1][j]
        for j in range(n):
            if dis[m-1][j]<mincost:
                mincost=dis[m-1][j]
                end=j
        #构建结果路径,从后往前
        res=[-1]*m
        for i in range(m-1,-1,-1):
            res[i]=end
            end=pre[i][end]
        return res
