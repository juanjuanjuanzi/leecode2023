# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
# def knows(a, b):

class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        """
        g=[[] for _ in range(n)]
        ind=[0]*n
        for i in range(n):
            if ind[i]>0:
                continue
            for j in range(n):
                if i==j:
                    continue
                if knows(j,i):
                    g[i].append(j)
                    ind[j]+=1
        #找到len==n-1.且ind==0的结点
        #print(g)
        for i in range(n):
            if len(g[i])==(n-1) and ind[i]==0:
                valid=True
                for v in g[i]:
                    if knows(i,v):
                        valid=False
                if valid:
                    return i
        return -1
