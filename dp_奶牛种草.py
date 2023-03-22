input:n,m,mat
mod=100000000
maxn=(1<<m)-1
legal=[0]*(maxn+1)
#找出合法的状态
for i in range(maxn):
    #左邻和右邻没有相连的草地
    if i&(i<<1) and i&(i>>1):
        legal[i]=1

#为每列重建输入的实际载体状态
init=[0]*(n+1)
for i in range(1,n+1):
    for j in range(1,m+1):
        init[i]=(init[i]<<1)+mat[i][j]

dp[0][0]=1#对前0行，此行状态是0的方案数为1
for i in range(1,n+1):
    for j in range(maxn+1):
        if legal[j] and (j&init[i]==j):#状态合法，且与土地状况吻合
            for k in range(maxn+1):#枚举上一行的方案，需要用上一行的状态来更新这一行，判断上下行是否不相邻
                if k&j:
                    dp[i][j]=(dp[i][j]+dp[i-1][k])%mod

#计算所有的方案数
total=0#0~n-1,用n的状态来总结所有的方案数
for i in range(maxn+1):
    total=(total+dp[n][i])%mod

return total

