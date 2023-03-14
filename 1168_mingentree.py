class Solution(object):
    def find(self,x):
        if x!=self.father[x]:
            self.father[x]=self.find(self.father[x])
        return self.father[x]

    def minCostToSupplyWater(self, n, wells, pipes):
        """
        :type n: int
        :type wells: List[int]
        :type pipes: List[List[int]]
        :rtype: int
        """
        self.father=[0]*(n+1)
        #reconstra+sort wells
        self.father[n]=n
        for i in range(n):
            pipes.append([0,(i+1),wells[i]])
            self.father[i]=i
        pipes.sort(key=lambda x: x[2])
        #print(pipes)
        edge_cnt=0
        ans=0
        #constru tree
        for x,y,w in pipes:
            root_x=self.find(x)
            root_y=self.find(y)
            if root_x!=root_y:
                self.father[root_x]=root_y
                edge_cnt+=1
                ans+=w
            if edge_cnt==n:
                return ans
        #return -1
