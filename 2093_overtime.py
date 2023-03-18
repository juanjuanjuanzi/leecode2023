class Solution(object):
    def minimumCost(self, n, highways, discounts):
        """
        :type n: int
        :type highways: List[List[int]]
        :type discounts: int
        :rtype: int
        """
        e=[[float('inf')]*n for _ in range(n)]
        g=[[]*n for _ in range(n)]
        for i,j,w in highways:
            g[i].append(j)
            g[j].append(i)
            e[i][j]=w
            e[j][i]=w
        for i in range(n):
            e[i][i]=0
        ans=[]
        res=[0]
        
        

        def dfs(x,pre):
            if x==(n-1):
                ans.append([i for i in res])
                return
            if len(g[x])==0:
                return
            for y in g[x]:
                if y!=pre:
                    #print(x,y,res)
                    if y in res:
                        continue
                    res.append(y)
                    #print(res)
                    dfs(y,x)
                    res.remove(y)
                    
        #print(g)
        dfs(0,None)
        
        
        if len(ans)==0:
            return -1
        mincost=float('inf')
        #print(ans)
        for path in ans:
            costs=[e[path[i]][path[i+1]] for i in range(len(path)-1)]
            #print(path,costs)
            costs.sort(reverse=True)
            for i in range(min(discounts,len(costs))):
                costs[i]=costs[i]//2
            total=0
            for i in range(len(path)-1):
                total+=costs[i]
            if total<mincost:
                mincost=total
        return mincost
        
        

