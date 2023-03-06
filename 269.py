class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        child={}
        n=len(words)
        degree={}
        for i in range(n-1):
            j=i+1
            m=min(len(words[i]),len(words[j]))
            for k in range(m):
                if words[i][k]!=words[j][k]:
                    w1=words[i][k]
                    w2=words[j][k]
                    child[w1]=w2
                    if w2 not in child:
                        child[w2]=None
                    if w2 in degree:
                        degree[w2]+=1
                    else:
                        degree[w2]=1
                    if w1 not in degree:
                        degree[w1]=0
                    break
                elif k==(m-1) and len(words[i])>len(words[j]):
                    return ""
        if len(degree)==0:
            return words[0][0]
        q=deque()
        for k in degree:           
            if degree[k]>1:
                return ""
            if degree[k]==0:
                q.append(k)
        if len(q)!=1:
            return ""
        ans=""
        head=q.pop()
        while head:
            ans+=head
            head=child[head]
        return ans
