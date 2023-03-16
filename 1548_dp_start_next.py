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
	    dis=[[None]*n for _ in range(m)]
        bestnext=[[None]*n for _ in range(m)]

        map={}      
        for i in range(n):
            map[i]=names[i]
        #target=[map[i] for i in targetPath]

        totalmindis=float('inf')
        startcity=0
        
        def dfs(curtarid,currootid):
            
            if curtarid==len(targetPath):#遍历终止的条件
                return 0
            if dis[curtarid][currootid]!=None:#说明当前节点已经处理过
                return dis[curtarid][currootid]
            curcost=0
            if map[currootid]!=targetPath[curtarid]:
                curcost=1
            #找出后面几个分支中距离最小的
            mincost=float('inf')
            for i in g[currootid]:
                
                d=dfs(curtarid+1,i)
                if d<mincost:
                    mincost=d
                    bestnext[curtarid][currootid]=i
                
            curcost+=mincost
            dis[curtarid][currootid]=curcost
            
            return curcost


        for i in range(n):
            d=dfs(0,i)
            
            if d<totalmindis:
                totalmindis=d
                startcity=i
        res=[]
        s=startcity
        #处理输出,startcity
        for i in range(m):
            res.append(s)            
            s=bestnext[i][s]
        return res
