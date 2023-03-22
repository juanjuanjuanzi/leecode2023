class Solution:
    def maximumCost(self, n: int, highways: List[List[int]], k: int) -> int:
        #constra graph
        g=[[] for _ in range(n)]
        for x,y,w in highways:
            g[x].append((y,w))
            g[y].append((x,w))
		
        @lru_cache(None)
        def dfs(x,explored):
            if explored.bit_count()==(k+1):
                return 0
            ans=-inf
            for y,w in g[x]:
                if not (explored&(o:=1<<y)):
                    ans=max(ans,dfs(y,explored|o)+w)
            return ans
		
        return max(-1,max(dfs(i,1<<i) for i in range(n)))

