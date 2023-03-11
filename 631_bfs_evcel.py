def coor(row, column):
    return [row-1,ord(column)-ord('A')]

class Excel(object):

    def __init__(self, height, width):
        """
        :type height: int
        :type width: str
        """
        self.h=height
        self.w=ord(width)-ord('A')+1
        self.n=self.h*self.w
        self.mat=[0 for _ in range(self.n)]
        self.g=[[] for _ in range(self.n)]
        self.father=[[] for _ in range(self.n)]
          
    def update_parents(self, x, y, val):
        idx=x*self.w+y
           
        #同时对依赖词节点的值进行全局更新
        vis=[False for _ in range(self.n)]
        q=[idx]
        while q:
            u=q.pop(0)
            vis[u]=True
            #print('ok1',self.father[u])
            for v in self.father[u]:#列出受u影响的节点
                if vis[v]==False:
                    num=0
                    #print('ok2',self.g[v])
                    for k in self.g[v]:#对每个节点重新计算值
                        num+=self.mat[k]
                    self.mat[v]=num
                
                    q.append(v)#继续更新上一级的节点

    def set(self, row, column, val):
        """
        :type row: int
        :type column: str
        :type val: int
        :rtype: None
        """
        i,j=coor(row,column)
        idx=i*self.w+j
        self.mat[idx]=val
        #切断其他节点对此节点的影响
        for v in self.g[idx]:
            if idx in self.father[v]:
                self.father[v].remove(idx)
        #清空此节点原来依赖的其他节点
        self.g[idx]=[]
        self.update_parents(i,j,val)
        
        #print(self.mat)

    
    def get(self, row, column):
        """
        :type row: int
        :type column: str
        :rtype: int
        """       
        x,y=coor(row,column)
        
        return self.mat[x*self.w+y]
        

    def sum(self, row, column, numbers):
        """
        :type row: int
        :type column: str
        :type numbers: List[str]
        :rtype: int
        """
        #print('start')
        #计算本身值,同时更新依赖此值的节点值
        x,y=coor(row, column)
        idx=x*self.w+y
        #删除此节点与之前依赖节点的绑定
        for v in self.g[idx]:#注意可能会出现b2=a1+a1的情况
            if idx in self.father[v]:          
                self.father[v].remove(idx)
        num=0
        tmp=[]
        for v in numbers:
            #print(v,len(v))
            if len(v)==2:
                r,c=coor(int(v[1]),v[0])
                index=r*self.w+c
                tmp.append(index)
                #这里做一个去重的判断
                if idx not in self.father[index]:
                    self.father[index].append(idx)
                num+=self.mat[index]
            else:
                #print(v)
                u=v.split(':')
                sx,sy=coor(int(u[0][1:]),u[0][0])
                ex,ey=coor(int(u[1][1:]),u[1][0])
                #print(sx,sy)
                #print(ex,ey)
                for i in range(sx,ex+1):
                    for j in range(sy,ey+1):
                        index=i*self.w+j
                        tmp.append(index)
                        if idx not in self.father[index]:
                            self.father[index].append(idx)
                        num+=self.mat[index]
                        #if self.mat[index]>0:
                        #    print(i,j,self.mat[index])
        
        self.g[idx]=tmp
        self.mat[idx]=num
        #这里只是希望更新下受(x,y)影响的父节点
        self.update_parents(x,y,num)
        #print('g',self.g)
        #print('f',self.father)
        #print('m',self.mat)
        return num






# Your Excel object will be instantiated and called as such:
# obj = Excel(height, width)
# obj.set(row,column,val)
# param_2 = obj.get(row,column)
# param_3 = obj.sum(row,column,numbers)
