class Solution(object):
    def treeDiameter(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: int
        """
        #满足树的形成条件，即无环路，n-1条边
        #根中top2两条遍历路径长度的叠加就是答案
        #前序遍历
        #肯定是用拓扑排序
        n=len(edges)+1
        
        g=[[] for _ in range(n)]
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
            
        res=[0]

        def dfs(cur,pre):
            #if len(g[cur])==1:
            #    return 0
            d1=d2=0#表示以cur为根的树的最深和次深，对于叶子节点值为0
            for i in g[cur]:#在以cur为根的树中，找出最深和次深的值
                if i!=pre:
                    d=dfs(i,cur)
                    if d>d1:
                        d1,d2=d,d1
                    elif d>d2:
                        d2=d
            res[0]=max(res[0],d1+d2)
            return d1+1##这里返回的是pre-cur一侧树的深度(>=1)
            
        dfs(0,None)
        return res[0]
