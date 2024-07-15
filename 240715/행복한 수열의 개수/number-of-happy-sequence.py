import sys
r=sys.stdin.readline

n,m=map(int,r().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

ans=0
for i in range(n):
    store=[0]*101
    for j in range(n):
        store[graph[i][j]]+=1
        if store[graph[i][j]] >= m:
            ans+=1
            break          


for i in range(n)::
    store=[0]*101
    for j in range(n):
        store[graph[j][i]]+=1
        if store[graph[j][i]] >= m:
            ans+=1
            break
print(ans)