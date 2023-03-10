class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: int
        """
        h=len(maze)
        w=len(maze[0])
        desx=destination[0]
        desy=destination[1]
        if desx!=(h-1) and desx!=0 and desy!=(w-1) and desy!=0:
            if maze[desx-1][desy]==0 and maze[desx+1][desy]==0 and maze[desx][desy-1]==0 and maze[desx][desy+1]==0:
                return -1

        dirs={(-1,0),(1,0),(0,-1),(0,1)}
        dist=[[float('inf')]*w for _ in range(h)]
        #vis=[[False]*w for _ in range(h)]
        #vis=False
        #当停下时，判断是否为终点，
        q=[(start[0],start[1])]
        dist[start[0]][start[1]]=0
        while q:
            i,j=q.pop(0)
            #vis[i][j]=True
            for dr,dc in dirs:
                x=i+dr
                y=j+dc
                step=dist[i][j]
                while 0<=x<h and 0<=y<w and maze[x][y]==0:
                    x+=dr
                    y+=dc
                    step+=1
                x-=dr
                y-=dc
                #if x==destination[0] and y==destination[1]:
                #    vis=True
                if dist[x][y]>step:
                    dist[x][y]=step
                    if x!=desx or y!=desy:
                        q.append((x,y))
                    #print(dist[x][y])
        #print(vis)
        return dist[desx][desy] if dist[desx][desy]!=float('inf') else -1

                
