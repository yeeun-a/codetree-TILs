import sys
r=sys.stdin.readline

n,m=map(int,r().split())
graph=[]
for _ in range(n):
    graph.append(list(map(int,r().split())))

ans=0
for i in range(n):
    last_num=graph[i][0]
    res=1
    for j in range(1,n):
        if last_num==graph[i][j]:
            res+=1
            if res >= m:
                ans+=1
                break
        else:
            res=1
            last_num=graph[i][j]

for i in range(n):
    last_num=graph[0][i]
    res=1
    for j in range(1,n):
        if last_num==graph[j][i]:
            res+=1
            if res >= m:
                ans+=1
                break
        else:
            res=1
            last_num=graph[j][i]
print(ans)