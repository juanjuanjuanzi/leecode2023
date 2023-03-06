class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        child={}
        g=defaultdict(list)
        n=len(words)
        degree={}
        #为words中的所有字母初始化入度
        for i in words:
            for j in i:
                degree[j]=0
        for i in range(n-1):
            j=i+1
            m=min(len(words[i]),len(words[j]))
            for k in range(m):
                if words[i][k]!=words[j][k]:
                    w1=words[i][k]
                    w2=words[j][k]
                    
                    g[w1].append(w2)
                    degree[w2]+=1
                    break
                elif k==(m-1) and len(words[i])>len(words[j]):
                    return ""
        
        q=[]
        for k in degree:           
            if degree[k]==0:
                q.append(k)
        for u in q:
            for v in g[u]:
                degree[v]-=1
                if degree[v]==0:
                    q.append(v)
        return ''.join(q) if len(q)==len(degree) else ""
