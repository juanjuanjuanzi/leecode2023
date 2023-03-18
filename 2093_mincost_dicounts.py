class Solution(object):
    def minimumCost(self, n, highways, discounts):
        """
        :type n: int
        :type highways: List[List[int]]
        :type discounts: int
        :rtype: int
        """
        g=[[] for _ in range(n)]
        for i,j,w in highways:
            g[i].append((j,w))
            g[j].append((i,w))

        ans=[[float('inf')]*(discounts+1) for _ in range(n)]
        ans[0][discounts]=0
        q=[(None,0,discounts)]
        while q:
            pre,x,disc=q.pop(0)
            for y,w in g[x]:
                if y==pre:
                    continue
                if disc>0:
                    if ans[y][disc-1]>ans[x][disc]+w//2:
                        ans[y][disc-1]=ans[x][disc]+w//2
                        q.append((x,y,disc-1))

                if ans[y][disc]>ans[x][disc]+w:
                    ans[y][disc]=ans[x][disc]+w
                    q.append((x,y,disc))
        m=min(ans[n-1])
        return m if m!=float('inf') else -1

                
        
        

