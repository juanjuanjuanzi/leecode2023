class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        h=len(maze)
        w=len(maze[0])
        g=[[] for _ in range(h*w)]
        vis=[False]*h*w
        edges=[]

        #在横竖俩个方向，基于墙生成边集合
        for r in range(h):
            r_eg=[]
            for c in range(w):
                idx=r*w+c
                if maze[r][c]==1:
                    #print(r_eg)
                    if len(r_eg)>1:
                        edges.append(r_eg)
                    r_eg=[]    
                elif maze[r][c]==0:
                    r_eg.append(idx)
            if len(r_eg)>1:
                edges.append(r_eg)
            
        for c in range(w):
            r_eg=[]
            for r in range(h):
                idx=r*w+c
                if maze[r][c]==1:
                    if len(r_eg)>1:
                        edges.append(r_eg)
                    r_eg=[]    
                elif maze[r][c]==0:
                    r_eg.append(idx)
            if len(r_eg)>1:
                edges.append(r_eg)

        #print(edges)
        #如果点在边上，则归入边的活动轨迹
        for edge in edges:
            for u in edge:
                if u!=edge[0]:
                    g[u].append(edge[0])
                if u!=edge[-1]:
                    g[u].append(edge[-1])
            
        #print(g)

        #BFS
        q=deque()
        ids=start[0]*w+start[1]
        ide=destination[0]*w+destination[1]
        q.append(ids)
        while q:
            u=q.popleft()
            vis[u]=True
            for v in g[u]:
                if v==ide:
                    return True
                if vis[v]==False:
                    q.append(v)
        return False
