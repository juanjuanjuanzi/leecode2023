input:n,m
dp=[[0]*2000 for _ in range(2000)]
mod=1000000007

def dfs(i,j,state,nex):
	if j==n:
  		#基于当前第i列的状态，
    	#第i+1列受影响生成的状态可以分别对应第i列的哪些操作，
     	#每次对应上了都将第i列的历史分数叠加一次
  		dp[i+1][nex]+=dp[i][state]
    	dp[i+1][nex]%=mod
    	return
      
	if state&(1<<j)>0:
    	dfs(i,j+1,state,nex)
      
  	if state&(1<<j)==0:
     	dfs(i,j+1.state,nex|(1<<j))
  
  	if state&(1<<j)==0 and state&(1<<(j+1)):
    	dfs(i,j+2,state,nex)
      
 	return	


dp[1][0]=1
#假定i从1开始
for i in range(1,m+1):
	for state in range(1<<n):
		if dp[i][state]:
			dfs(i,0,state,0)
#这里为什么是m+1
#因为dp[i][state]表示上一列有多少种状态可以生成当前第i列的状态state，
#因此最终应该是dp[m+1][0]对应的方案数
return dp[m+1][0]	

	
