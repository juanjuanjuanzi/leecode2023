# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
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
        #先摸索出网格全貌
        start=(0,0)
        end=[None]
        dirs=[(-1,0,'U'),(1,0,'D'),(0,1,'R'),(0,-1,'L')]
        coor=set()
        coor.add((0,0))
        grid=[[float('inf')]*500 for _ in range(500)]
        minx=[0]
        miny=[0]

        def goback(d): # 回退相反的移动
            if d == "U":
                master.move("D")
            elif d == "D":
                master.move("U")
            elif d == "L":
                master.move("R")
            else:
                master.move("L")

        def dfs(x,y):
            #print(x,y)
            if end[0]==None:
                if master.isTarget():                   
                    end[0]=(x,y)
            for dx,dy,ch in dirs:
                nx=x+dx
                ny=y+dy
                if master.canMove(ch) and (nx,ny) not in coor:
                    
                    if nx<minx[0]:
                        minx[0]=nx
                    if ny<miny[0]:
                        miny[0]=ny
                    
                    coor.add((nx,ny))
                    master.move(ch)
                    dfs(nx,ny)
                    goback(ch)

        dfs(0,0)
               
        if end[0]==None:
            return -1
        
        for x,y in coor: 
            x-=minx[0]
            y-=miny[0]
            grid[x][y]=1
        sx=start[0]-minx[0]
        sy=start[1]-miny[0]        
        ex=end[0][0]-minx[0]
        ey=end[0][1]-miny[0]
        
        grid[ex][ey]=2
        grid[sx][sy]=-1
        
        #short path       
        dis=[[float('inf')]*500 for _ in range(500)]
        q=[(sx,sy)]
        dis[sx][sy]=0
        
        
        while q:
            #print(q)
            x,y=q.pop(0)
            for dx,dy,ch in dirs:
                nx=x+dx
                ny=y+dy
                if 0<=nx<500 and 0<=ny<500 and grid[nx][ny] in [-1,1,2] and dis[x][y]+1<dis[nx][ny]:
                    dis[nx][ny]=dis[x][y]+1
                    if (nx,ny)!=(ex,ey):
                        q.append((nx,ny))
        
        return dis[ex][ey] if dis[ex][ey]!=float('inf') else -1
        
