class UnionFind:
    def __init__(self,n):
        self.n=n
        self.part=n
        self.parent=[i for i in range(n)]
        self.size=[1]*n
        self.rank=[1]*n

    def Find(self,x):
        if self.parent[x]!=x:
            self.parent[x]=self.Find(self.parent[x])
        return self.parent[x]
    
    def Union(self,x,y):
        root_x=self.Find(x)
        root_y=self.Find(y)
        if root_x==root_y:
            return False
        if self.size[x]>self.size[y]:
            root_x,root_y=root_y,root_x
        self.parent[root_x]=root_y
        self.size[root_y]+=self.size[root_x]
        self.part-=1
    
    def is_same_part(self,x,y):
        return self.Find(x)==self.Find(y)

    def get_part_size(self,x):
        root_x=self.Find(x)
        return self.size[root_x]

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        UF=UnionFind(n)
        for x,y in edges:
            UF.Union(x,y)
        return UF.part
        
