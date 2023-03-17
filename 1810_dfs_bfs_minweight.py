# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about it's implementation
# """
#class GridMaster(object):
#    def canMove(self, direction):
#        """
#        :type direction: str
#        :rtype bool
#        """
#
#    def move(self, direction):
#        """
#        :type direction: str
#.       :rtype int
#        """
#
#    def isTarget(self):
#        """
#        :rtype bool
#        """
#

class Solution(object):
    def findShortestPath(self, master):
        """
        :type master: GridMaster
        :rtype: int
        """
        g=set()
        g.add((0,0,0))
        coor=set()
        coor.add((0,0))
        start=(0,0)
        end=[None]
        dirs=[(-1,0,'U'),(1,0,'D'),(0,-1,'L'),(0,1,'R')]
        minx=[0]
        miny=[0]

        def goback(d):
            if d=='U':
                master.move('D')
            elif d=='D':
                master.move('U')
            elif d=='L':
                master.move('R')
            elif d=='R':
                master.move('L')

        def dfs(x,y):
            
            if end[0]==None:
                if master.isTarget():
                    end[0]=(x,y)
            for dx,dy,ch in dirs:
                nx=x+dx
                ny=y+dy
                if master.canMove(ch) and (nx,ny) not in coor: 
                    #print(x,y,nx,ny,coor) 
                    minx[0]=min(nx,minx[0])  
                    miny[0]=min(ny,miny[0])                  
                    w=master.move(ch)
                    g.add((nx,ny,w))
                    coor.add((nx,ny))
                    dfs(nx,ny)
                    goback(ch)
            
        dfs(0,0)
        if end[0]==None:
            return -1
        grid=[[float('inf')]*100 for _ in range(100)]
        dis=[[float('inf')]*100 for _ in range(100)]
        sx,sy=start[0]-minx[0],start[1]-miny[0]
        ex,ey=end[0][0]-minx[0],end[0][1]-miny[0]
        for x,y,w in g:
            nx,ny=x-minx[0],y-miny[0]
            grid[nx][ny]=w
        #print(sx,sy,ex,ey)
        #print(grid[0][0:2],grid[1][0:2])
        q=[(sx,sy)]
        dis[sx][sy]=0
        while q:
            x,y=q.pop(0)
            for dx,dy,ch in dirs:
                nx=x+dx
                ny=y+dy
                if 0<=nx<100 and 0<=ny<100 and grid[nx][ny]<=100:
                    nw=grid[nx][ny]
                    if dis[x][y]+nw<dis[nx][ny]:
                        dis[nx][ny]=dis[x][y]+nw
                        if (nx,ny)!=(ex,ey):
                            q.append((nx,ny))                        
                    
        return dis[ex][ey] if dis[ex][ey]!=float('inf') else -1
