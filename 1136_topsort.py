class Solution(object):
    def minimumSemesters(self, n, relations):
        """
        :type n: int
        :type relations: List[List[int]]
        :rtype: int
        """
        ind=[0]*n
        g=[[] for _ in range(n)]
        for x,y in relations:
            g[x-1].append(y-1)
            ind[y-1]+=1
        q=[i for i in range(n) if ind[i]==0]
        #print(q)
        p=[0]
        num_vex=0
        num_xq=0
        while p:
            p=[]
            while q:
                u=q.pop(0)
                num_vex+=1
                for v in g[u]:
                    ind[v]-=1
                    if ind[v]==0:
                        p.append(v)
            num_xq+=1
            q=[i for i in p]
        
        if num_vex==n:
            return num_xq
        else:
            return -1
